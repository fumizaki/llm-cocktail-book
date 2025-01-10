"use server";

import { auth } from "@/auth/config";
// import { convertSnakeToCamel } from "@/lib/convert-case";
import type { GetAllActionState } from "./type";

export async function getAllAction(): Promise<GetAllActionState> {
	const session = await auth();
	const res = await fetch(`${process.env.API_BASE_URL}/chatbot`, {
		headers: {
			Authorization: `Bearer ${session?.user.authorization.accessToken}`,
		},
	});

	if (!res.ok) {
		throw new Error("Error get all chatbot: " + res.statusText);
	}

	return {
		ok: true,
		status: 200,
		data: await res.json(),
	};
}
