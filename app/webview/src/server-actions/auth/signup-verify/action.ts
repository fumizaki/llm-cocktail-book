"use server";

import type { VerifyActionState } from "./type";

export async function verifyAction(
	key: string | string[] | undefined,
): Promise<VerifyActionState> {
	const res = await fetch(
		`${process.env.API_BASE_URL}/oauth/signup/verify?key=${key}`,
	);

	if (!res.ok) {
		throw new Error("Error get all chatbot: " + res.statusText);
	}

	return {
		ok: true,
		status: 200,
		data: await res.json(),
	};
}
