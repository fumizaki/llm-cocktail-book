'use server'

import { AuthorizationGrant } from "@/domain/value";
import { convertCamelToSnake, convertSnakeToCamel } from "@/lib/convert-case";
import { SigninActionState } from "./type";

export async function signinAction(email: string, password: string): Promise<SigninActionState> {
    const res = await fetch(`${process.env.API_BASE_URL}/oauth/signin`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(convertCamelToSnake({ grantType: AuthorizationGrant.PASSWORD, email: email, password: password })),
    });

    if (!res.ok) {
        throw new Error('Error sign-in: ' + res.statusText);
    }

    return {
        ok: true,
        status: 200,
        data: convertSnakeToCamel(await res.json())
    }
}