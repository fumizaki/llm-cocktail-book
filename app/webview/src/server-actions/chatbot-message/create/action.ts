"use server";

import { auth } from "@/auth/config";
import { parseSnakeToCamel, parseCamelToSnake } from "@/lib/parse-case";
import { parseObjectToFormData } from "@/lib/parse-form";
import { parseFormDataToObject } from "@/lib/parse-form";
import type { NewChatbotMessage } from "@/domain/schema";
import { insertChatbotMessage } from "@/domain/validation";
import type { CreateActionState } from "./type";

export async function createAction(
	prevState: CreateActionState,
	formData: FormData,
): Promise<CreateActionState> {
	const session = await auth();

	// formDataを変換する
	const params = parseFormDataToObject<{ inputs: NewChatbotMessage }>(formData);
	const validatedFields = insertChatbotMessage.safeParse(params.inputs);
	if (!validatedFields.success) {
		return {
			success: false,
			message: "Validation Error",
			validationErrors: validatedFields.error.flatten().fieldErrors,
			inputs: params.inputs,
		};
	}
	// const newFormData = new FormData();
	// newFormData.append("chatbot_id", validatedFields.data.chatbotId);
	// newFormData.append("resource", validatedFields.data.resource);
	// newFormData.append("mode", validatedFields.data.mode);
	// newFormData.append("prompt", validatedFields.data.prompt);

	// // 画像ファイルを追加
	// if (validatedFields.data.images) {
	// 	validatedFields.data.images.forEach((image) => newFormData.append("images", image));
	// }

	// // ドキュメントファイルを追加
	// if (validatedFields.data.docs) {
	// 	validatedFields.data.docs.forEach((doc) => newFormData.append("docs", doc));
	// }

	const res = await fetch(`${process.env.API_BASE_URL}/chatbot/message`, {
		method: "POST",
		headers: {
			Authorization: `Bearer ${session?.user.authorization.accessToken}`,
		},
		body: parseObjectToFormData(parseCamelToSnake(validatedFields.data)),
	});

	if (!res.ok) {
		return {
			success: false,
			message: "Server Error",
			serverErrors: `[${res.status}] ${res.statusText}`,
			inputs: params.inputs,
		};
	}
	return {
		success: true,
		inputs: {
			chatbotId: params.inputs.chatbotId,
			resource: params.inputs.resource,
			mode: params.inputs.mode,
			prompt: "",
			images: [],
			docs: []
		},
		data: parseSnakeToCamel(await res.json()),
	};
}
