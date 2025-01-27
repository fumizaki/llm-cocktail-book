"use server";

import { auth } from "@/auth/config";
import { parseSnakeToCamel } from "@/lib/parse-case";


export async function paymentCheckoutAction(

): Promise<string> {
    const session = await auth()

    const res = await fetch(`${process.env.API_BASE_URL}/payment/checkout`, {
		method: "POST",
		headers: {
			Authorization: `Bearer ${session?.user.authorization.accessToken}`,
			"Content-Type": "application/json",
		},
	});

    return parseSnakeToCamel(await res.json()).clientSecret
}