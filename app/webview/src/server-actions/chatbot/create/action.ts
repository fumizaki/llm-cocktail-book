"use server";

import { auth } from "@/auth/config";
import { parseSnakeToCamel } from "@/lib/parse-case";
import { parseFormDataToObject } from "@/lib/parse-form";
import type { NewChatbot } from "@/domain/schema";
import { insertChatbot } from "@/domain/validation";
import type { CreateActionState } from "./type";

export async function createAction(
	prevState: CreateActionState,
	formData: FormData,
): Promise<CreateActionState> {
	const session = await auth();

	// formDataを変換する
	const params = parseFormDataToObject<{ inputs: NewChatbot }>(formData);
	const validatedFields = insertChatbot.safeParse(params.inputs);

	if (!validatedFields.success) {
		return {
			success: false,
			message: "Validation Error",
			validationErrors: validatedFields.error.flatten().fieldErrors,
			inputs: params.inputs,
		};
	}
	const res = await fetch(`${process.env.API_BASE_URL}/chatbot`, {
		method: "POST",
		headers: {
			Authorization: `Bearer ${session?.user.authorization.accessToken}`,
			"Content-Type": "application/json",
		},
		body: JSON.stringify(validatedFields.data),
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
