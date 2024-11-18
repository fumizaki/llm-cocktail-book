'use server'

import { AuthorizationGrant } from "@/domain/value";
import { convertCamelToSnake, convertSnakeToCamel } from "@/lib/convert-case";

export async function signinAction(email: string, password: string): Promise<any> {
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

    return convertSnakeToCamel(res.json());
}