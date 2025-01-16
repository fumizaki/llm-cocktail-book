"use server";

import { AuthorizationGrant } from "@/domain/value";
import { parseCamelToSnake, parseSnakeToCamel } from "@/lib/parse-case";
import type { SigninActionState } from "./type";

export async function signinAction(
	email: string,
	password: string,
): Promise<SigninActionState> {
	const res = await fetch(`${process.env.API_BASE_URL}/oauth/signin`, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(
			parseCamelToSnake({
				grantType: AuthorizationGrant.PASSWORD,
				email: email,
				password: password,
			}),
		),
	});

	if (!res.ok) {
		return {
			success: false,
			message: "Server Error",
			serverErrors: `[${res.status}] ${res.statusText}`,
			inputs: {
				email: email,
				password: password,
			},
		};
	}

	return {
		success: true,
		data: parseSnakeToCamel(await res.json()),
	};
}
