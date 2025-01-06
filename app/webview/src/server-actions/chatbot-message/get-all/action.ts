'use server'

import { auth } from "@/auth/config";
import { GetAllActionState } from "./type";

export async function getAllAction(chatbotId: string): Promise<GetAllActionState> {
    const session = await auth()
    const res = await fetch(`${process.env.API_BASE_URL}/chatbot/message/${chatbotId}`, {
        headers: {
            'Authorization': `Bearer ${session?.user.authorization.accessToken}`
        },
    });

    if (!res.ok) {
        throw new Error('Error get all chatbot: ' + res.statusText)
    }
    return {
        ok: true,
        status: 200,
        data: await res.json()
    }
}