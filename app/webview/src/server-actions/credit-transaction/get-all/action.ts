"use server";

import { auth } from "@/auth/config";
import { parseSnakeToCamel } from "@/lib/parse-case";
import type { GetAllActionState } from "./type";

export async function getAllAction(
): Promise<GetAllActionState> {
	const session = await auth();
	const res = await fetch(
		`${process.env.API_BASE_URL}/credit/transaction`,
		{
			headers: {
				Authorization: `Bearer ${session?.user.authorization.accessToken}`,
			},
		},
	);

	if (!res.ok) {
		throw new Error("Error get all credit transaction: " + res.statusText);
	}

	return {
		data: parseSnakeToCamel(await res.json())
	};
}
