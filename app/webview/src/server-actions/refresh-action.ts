'use server'

import { AuthorizationGrant } from "@/domain/value";

import { convertCamelToSnake, convertSnakeToCamel } from "@/lib/convert-case";

export async function refreshAction(refreshToken: string): Promise<any> {
    const res = await fetch(`${process.env.API_BASE_URL}/oauth/refresh`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(convertCamelToSnake({ grantType: AuthorizationGrant.REFRESH_TOKEN, refreshToken: refreshToken })),
    });

    if (!res.ok) {
        throw new Error('Error refresh: ' + res.statusText);
    }

    return convertSnakeToCamel(res.json());
}