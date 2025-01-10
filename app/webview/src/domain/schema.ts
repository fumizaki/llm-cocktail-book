import type { z } from "zod";
import type * as validation from "@/domain/validation";

// Auth
export type AuthToken = z.infer<typeof validation.selectAuthToken>;
export type SignUpRequestParams = z.infer<typeof validation.signUpRequest>;
export type SignInRequestParams = z.infer<typeof validation.signInRequest>;
export type RefreshTokenRequestParams = z.infer<
	typeof validation.refreshTokenRequest
>;

// Chatbot
export type Chatbot = z.infer<typeof validation.selectChatbot>;
export type NewChatbot = z.infer<typeof validation.insertChatbot>;
export type ChatbotMessage = z.infer<typeof validation.selectChatbotMessage>;
export type NewChatbotMessage = z.infer<typeof validation.insertChatbotMessage>;
