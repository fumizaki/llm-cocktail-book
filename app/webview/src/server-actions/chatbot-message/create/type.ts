import type { ChatbotMessage, NewChatbotMessage } from "@/domain/schema";

export interface CreateActionState {
	success?: boolean;
	message?: string;
	validationErrors?: Record<string, string[]>;
	serverErrors?: string;
	inputs?: NewChatbotMessage;
	data?: ChatbotMessage;
}
