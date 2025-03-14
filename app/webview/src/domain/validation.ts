import { z } from "zod";
import * as value from "@/domain/value";

// Auth

export const selectAuthToken = z.object({
	accessToken: z.string(),
	tokenType: z.nativeEnum(value.AuthorizationToken),
	expiresIn: z.number().positive(),
	refreshToken: z.string(),
	scope: z.string().optional(),
	idToken: z.string().optional(),
});

export const signUpRequest = z.object({
	email: z.string().email(),
	password: z
		.string()
		.trim()
		.min(8, { message: "パスワードは8文字以上で入力してください" }),
	redirectUrl: z.string().optional()
});

export const signInRequest = signUpRequest.extend({
	grantType: z.nativeEnum(value.AuthorizationGrant),
	scope: z.string().optional(),
});

export const refreshTokenRequest = z.object({
	grantType: z.nativeEnum(value.AuthorizationGrant),
	refreshToken: z
		.string()
		.trim()
		.min(1, { message: "リフレッシュトークンが空です" }),
	scope: z.string().optional(),
});

// Chatbot
export const selectChatbot = z.object({
	id: z.string().uuid(),
	title: z.string().trim().min(1, { message: "1文字以上で入力してください" }),
});

export const insertChatbot = z.object({
	title: z.string().trim().min(1, { message: "1文字以上で入力してください" }),
});

export const selectChatbotMessage = z.object({
	id: z.string().uuid(),
	chatbotId: z.string().uuid(),
	content: z.string().trim().min(1, { message: "1文字以上で入力してください" }),
	role: z.nativeEnum(value.MessageRole),
});

export const insertChatbotMessage = z.object({
	chatbotId: z.string().uuid(),
	resource: z.string(),
	mode: z.string(),
	prompt: z.string().trim().min(1, { message: "1文字以上で入力してください" }),
	images: z.array(z.custom<File>()).optional(),
	docs: z.array(z.custom<File>()).optional()
});

export const selectChatbotIndex = z.object({
	id: z.string().uuid(),
	chatbotId: z.string().uuid(),
	title: z.string().trim().min(1, { message: "1文字以上で入力してください" }),
	content: z.string().trim().min(1, { message: "1文字以上で入力してください" }),
});

export const insertChatbotIndex = z.object({
	chatbotId: z.string().uuid(),
	resource: z.string(),
	title: z.string().trim().min(1, { message: "1文字以上で入力してください" }),
	content: z.string().trim().min(1, { message: "1文字以上で入力してください" }),
	docs: z.array(z.custom<File>()).optional()
});

// Credit
export const selectCredit = z.object({
	id: z.string().uuid(),
	accountId: z.string().uuid(),
	balance: z.number()
})

export const selectCreditTransaction = z.object({
	id: z.string().uuid(),
	accountId: z.string().uuid(),
	transactionType: z.string(),
	credit: z.number(),
	description: z.string()
})


export const chargeCredit = z.object({
	amount: z.number().min(500, { message: "500円以上で入力してください" }),
	currency: z.string().trim().min(3, { message: "3文字で入力してください" }).max(3, { message: "3文字で入力してください" })
});
export const orderedCredit = z.object({
	amount: z.number().min(500, { message: "500円以上で入力してください" }),
	currency: z.string().trim().min(3, { message: "3文字で入力してください" }).max(3, { message: "3文字で入力してください" }),
	clientSecret: z.string()
})