'use server'

import { auth } from "@/auth/config";
// import { convertSnakeToCamel } from "@/lib/convert-case";
import { Chatbot } from "@/domain/schema";

export async function getAllAction(): Promise<Chatbot[]> {
    const session = await auth()
    const res = await fetch(`${process.env.API_BASE_URL}/chatbot`, {
        headers: {
            'Authorization': `Bearer ${session?.user.authorization.accessToken}`
        },
    });

    if (!res.ok) {
        throw new Error('Error get all chatbot: ' + res.statusText)
    }

    return await res.json()
}