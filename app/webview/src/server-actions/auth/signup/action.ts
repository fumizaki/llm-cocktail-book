"use server";

import { parseCamelToSnake } from "@/lib/parse-case";
import { parseFormDataToObject } from "@/lib/parse-form";
import type { SignUpRequestParams } from "@/domain/schema";
import { signUpRequest } from "@/domain/validation";
import type { SignupActionState } from "./type";

export async function signupAction(
	prevState: SignupActionState,
	formData: FormData,
): Promise<SignupActionState> {
	// formDataを変換する
	const params = parseFormDataToObject<SignUpRequestParams>(formData);
	const validatedParams = signUpRequest.safeParse(params);
	if (!validatedParams.success) {
		return {
			...prevState,
			validationErrors: validatedParams.error.issues?.map(
				(issue) => issue.message,
			),
		};
	}
	const res = await fetch(`${process.env.API_BASE_URL}/oauth/signup`, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(params),
	});

	if (!res.ok) {
		throw new Error("Error sign-up: " + res.statusText);
	}

	return {
		email: "",
		password: "",
	};
}
