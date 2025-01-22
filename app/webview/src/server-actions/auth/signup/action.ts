"use server";

import { redirect } from "next/navigation";
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
	const params = parseFormDataToObject<{ inputs: SignUpRequestParams }>(
		formData,
	);

	const validatedFields = signUpRequest.safeParse(params.inputs);
	if (!validatedFields.success) {
		return {
			success: false,
			message: "Validation Error",
			validationErrors: validatedFields.error.flatten().fieldErrors,
			inputs: params.inputs,
		};
	}
	const res = await fetch(`${process.env.API_BASE_URL}/oauth/signup`, {
		method: "POST",
		headers: {
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

	redirect("/auth/signup/confirmination");
}
