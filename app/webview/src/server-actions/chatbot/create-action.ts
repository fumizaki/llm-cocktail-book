'use server'

import { auth } from "@/auth/config";
// import { convertSnakeToCamel } from "@/lib/convert-case";
import { Chatbot, NewChatbot } from "@/domain/schema";

export async function createAction(params: NewChatbot): Promise<Chatbot> {
    const session = await auth()
    const res = await fetch(`${process.env.API_BASE_URL}/chatbot`, {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${session?.user.authorization.accessToken}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(params)
    });

    if (!res.ok) {
        throw new Error('Error get all chatbot: ' + res.statusText)
    }

    return await res.json()
}