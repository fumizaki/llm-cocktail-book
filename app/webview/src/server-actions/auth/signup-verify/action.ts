"use server";

import type { VerifyActionState } from "./type";
import { redirect } from "next/navigation";

export async function verifyAction(
	key: string | string[] | undefined,
): Promise<VerifyActionState> {
	const res = await fetch(
		`${process.env.API_BASE_URL}/oauth/signup/verify?key=${key}`,
	);

	if (!res.ok) {
		throw new Error("Error: " + res.statusText);
	}

	redirect(await res.json());
}
