"use server";

import { auth } from "@/auth/config";
// import { parseSnakeToCamel } from "@/lib/parse-case";
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
	const params = parseFormDataToObject<NewChatbot>(formData);
	const validatedFields = insertChatbot.safeParse(params);
	
	if (!validatedFields.success) {
		// const fieldErrors = validatedFields.error.flatten().fieldErrors;
		// Object.entries(fieldErrors).forEach(([fieldName, errors]) => {
		// 	// 
		// });
		return {
			...prevState,
			validationErrors: validatedFields.error.issues
				?.map((issue) => issue.message)
				?.join("\n"),
		};
	}
	const res = await fetch(`${process.env.API_BASE_URL}/chatbot`, {
		method: "POST",
		headers: {
			Authorization: `Bearer ${session?.user.authorization.accessToken}`,
			"Content-Type": "application/json",
		},
		body: JSON.stringify(params),
	});

	if (!res.ok) {
		return {
			...prevState,
			serverErrors: res.statusText,
		};
	}

	return {
		title: "",
		data: await res.json(),
	};
}
