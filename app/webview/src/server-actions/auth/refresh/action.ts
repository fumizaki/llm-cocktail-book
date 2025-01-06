'use server'

import { AuthorizationGrant } from "@/domain/value";
import { convertCamelToSnake, convertSnakeToCamel } from "@/lib/convert-case";
import { RefreshActionState } from "./type";


export async function refreshAction(refreshToken: string): Promise<RefreshActionState> {
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

    return {
        ok: true,
        status: 200,
        data: convertSnakeToCamel(await res.json())
    }
}