'use server'

import { auth } from "@/auth/config";
import { parseSnakeToCamel } from "@/lib/parse-case";
import { parseFormDataToObject } from "@/lib/parse-form";
import { NewChatbotMessage } from "@/domain/schema";
import { insertChatbotMessage } from "@/domain/validation";
import { CreateActionState } from "./type";

export async function createAction(prevState: CreateActionState, formData: FormData): Promise<CreateActionState> {
    const session = await auth()
    // formDataを変換する
    const params = parseFormDataToObject<NewChatbotMessage>(formData)
    const validatedParams = insertChatbotMessage.safeParse(params)
    if (!validatedParams.success) {
        return {
            ...prevState,
            validationErrors: validatedParams.error.issues?.map((issue) => issue.message)?.join("\n")
        }
    }
    
    const res = await fetch(`${process.env.API_BASE_URL}/chatbot/message`, {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${session?.user.authorization.accessToken}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({chatbot_id: params.chatbotId, meta: params.meta, prompt: params.prompt})
    });

    if (!res.ok) {
        return {
            ...prevState,
            serverErrors: res.statusText
        }
    }
    return {
        chatbotId: prevState.chatbotId,
        prompt: '',
        meta: {
            llm: prevState.meta.llm,
            mode: prevState.meta.mode
        },
        data: await res.json()
    }
}