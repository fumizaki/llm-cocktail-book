'use server'

import { AuthorizationGrant } from "@/domain/value";
import { parseCamelToSnake, parseSnakeToCamel } from "@/lib/parse-case";
import { SigninActionState } from "./type";

export async function signinAction(email: string, password: string): Promise<SigninActionState> {
    const res = await fetch(`${process.env.API_BASE_URL}/oauth/signin`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(parseCamelToSnake({ grantType: AuthorizationGrant.PASSWORD, email: email, password: password })),
    });

    if (!res.ok) {
        throw new Error('Error sign-in: ' + res.statusText);
    }

    return {
        ok: true,
        status: 200,
        data: parseSnakeToCamel(await res.json())
    }
}