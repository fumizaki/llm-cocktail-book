"use server";

import { AuthorizationGrant } from "@/domain/value";
import { parseCamelToSnake, parseSnakeToCamel } from "@/lib/parse-case";
import type { RefreshActionState } from "./type";

export async function refreshAction(
	refreshToken: string,
): Promise<RefreshActionState> {
	const res = await fetch(`${process.env.API_BASE_URL}/oauth/refresh`, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(
			parseCamelToSnake({
				grantType: AuthorizationGrant.REFRESH_TOKEN,
				refreshToken: refreshToken,
			}),
		),
	});

	if (!res.ok) {
		throw new Error("Error refresh: " + res.statusText);
	}

	return {
		data: parseSnakeToCamel(await res.json()),
	};
}
