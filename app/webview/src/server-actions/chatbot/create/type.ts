import type { Chatbot, NewChatbot } from "@/domain/schema";

export interface CreateActionState extends NewChatbot {
	validationErrors?: string | Record<string, string[]>;
	serverErrors?: string | Record<string, string[]>;
	data?: Chatbot;
}
