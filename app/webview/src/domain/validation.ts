import { z } from 'zod';
import * as value from '@/domain/value'

// Auth

export const selectAuthToken = z.object({
    accessToken: z.string(),
    tokenType: z.nativeEnum(value.AuthorizationToken),
    expiresIn: z.number(),
    refreshToken: z.string(),
    scope: z.string().optional(),
    idToken: z.string().optional()
})

export const signUpRequest = z.object({
    email: z.string().email(),
    password: z.string().trim().min(8, { message: 'パスワードは8文字以上で入力してください'})
});

export const signInRequest = signUpRequest.extend({
    grantType: z.nativeEnum(value.AuthorizationGrant),
    scope: z.string().optional()
})

export const refreshTokenRequest = z.object({
    grantType: z.nativeEnum(value.AuthorizationGrant),
    refreshToken: z.string(),
    projectId: z.string(),
    projectSecret: z.string(),
    scope: z.string().optional()
});


// Chatbot
export const selectChatbot = z.object({
    id: z.string().uuid(),
    title: z.string(),
})

export const insertChatbot = z.object({
    title: z.string().trim()
})


export const selectChatbotMessage = z.object({
    id: z.string().uuid(),
    chatbotId: z.string().uuid(),
    content: z.string(),
    role: z.nativeEnum(value.MessageRole)
})

export const insertChatbotMessage = z.object({
    mode: z.string(),
    meta: z.object({ llm: z.string() }),
    prompt: z.string().trim(),
    context: z.array(z.object({ role: z.nativeEnum(value.MessageRole), prompt: z.string() }))
})