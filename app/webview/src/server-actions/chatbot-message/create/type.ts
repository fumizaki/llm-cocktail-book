import type { ChatbotMessage, NewChatbotMessage } from "@/domain/schema";

export interface CreateActionState extends NewChatbotMessage {
	validationErrors?: string | Record<string, string[]>;
	serverErrors?: string | Record<string, string[]>;
	data?: ChatbotMessage;
}
