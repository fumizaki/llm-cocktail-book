"use server";

import { auth } from "@/auth/config";
import { parseSnakeToCamel } from "@/lib/parse-case";
import { parseFormDataToObject } from "@/lib/parse-form";
import type { ChargeCredit } from "@/domain/schema";
import { chargeCredit } from "@/domain/validation";
import type { ChargeActionState } from "./type";

export async function chargeAction(
	prevState: ChargeActionState,
	formData: FormData,
): Promise<ChargeActionState> {
	const session = await auth();

	// formDataを変換する
	const params = parseFormDataToObject<{ inputs: ChargeCredit }>(formData);
	const parsedParams: ChargeCredit = { amount: Number(params.inputs.amount), currency: params.inputs.currency }
	const validatedFields = chargeCredit.safeParse(parsedParams);
	if (!validatedFields.success) {
		return {
			success: false,
			message: "Validation Error",
			validationErrors: validatedFields.error.flatten().fieldErrors,
			inputs: parsedParams,
		};
	}
	const res = await fetch(`${process.env.API_BASE_URL}/credit/order`, {
		method: "POST",
		headers: {
			Authorization: `Bearer ${session?.user.authorization.accessToken}`,
			"Content-Type": "application/json",
		},
		body: JSON.stringify(validatedFields.data),
	});

	if (!res.ok) {
		return {
			success: false,
			message: "Server Error",
			serverErrors: `[${res.status}] ${res.statusText}`,
			inputs: parsedParams,
		};
	}
	return {
		success: true,
		data: parseSnakeToCamel(await res.json()),
	};
}
