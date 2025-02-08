import type { ChatbotIndex, NewChatbotIndex } from "@/domain/schema";

export interface CreateActionState {
	success?: boolean;
	message?: string;
	validationErrors?: Record<string, string[]>;
	serverErrors?: string;
	inputs?: NewChatbotIndex;
	data?: ChatbotIndex;
}
