'use server'

import { AuthorizationGrant } from "@/domain/value";


export async function refreshAction(refreshToken: string): Promise<any> {
    const res = await fetch(`${process.env.API_BASE_URL}/oauth/refresh`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ grant_type: AuthorizationGrant.REFRESH_TOKEN, refresh_token: refreshToken }),
    });

    if (!res.ok) {
        throw new Error('Error refresh: ' + res.statusText);
    }

    return res.json();
}