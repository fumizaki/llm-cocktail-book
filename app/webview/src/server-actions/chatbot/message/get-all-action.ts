'use server'

import { auth } from "@/auth/config";
import { ChatbotMessage } from "@/domain/schema";

export async function getAllAction(chatbotId: string): Promise<ChatbotMessage[]> {
    const session = await auth()
    const res = await fetch(`${process.env.API_BASE_URL}/chatbot/${chatbotId}/message`, {
        headers: {
            'Authorization': `Bearer ${session?.user.authorization.accessToken}`
        },
    });

    if (!res.ok) {
        throw new Error('Error get all chatbot: ' + res.statusText)
    }

    return await res.json()
}