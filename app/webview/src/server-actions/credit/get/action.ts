"use server";

import { auth } from "@/auth/config";
import { parseSnakeToCamel } from "@/lib/parse-case";
import type { GetActionState } from "./type";

export async function getAction(): Promise<GetActionState> {
	const session = await auth();
	const res = await fetch(`${process.env.API_BASE_URL}/credit`, {
		headers: {
			Authorization: `Bearer ${session?.user.authorization.accessToken}`,
		},
	});

	if (!res.ok) {
		throw new Error("Error get credit: " + res.statusText);
	}

	return {
		data: parseSnakeToCamel(await res.json()),
	};
}
