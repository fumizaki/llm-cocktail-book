"use server";

import { auth } from "@/auth/config";
import { parseSnakeToCamel, parseCamelToSnake } from "@/lib/parse-case";
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

	const res = await fetch(`${process.env.API_BASE_URL}/chatbot/message`, {
		method: "POST",
		headers: {
			Authorization: `Bearer ${session?.user.authorization.accessToken}`,
			"Content-Type": "application/json",
		},
		body: JSON.stringify(parseCamelToSnake(validatedFields.data)),
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
		data: parseSnakeToCamel(await res.json()),
	};
}
