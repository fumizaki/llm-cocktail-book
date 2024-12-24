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


// Chat
export const selectMessage = z.object({
    id: z.string().uuid(),
    content: z.string(),
    role: z.nativeEnum(value.MessageRole)
})

export const insertMessage = z.object({
    prompt: z.string().trim()
})