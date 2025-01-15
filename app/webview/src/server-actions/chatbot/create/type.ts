import type { Chatbot, NewChatbot } from "@/domain/schema";

export interface CreateActionState {
	success?: boolean;
	message?: string;
	validationErrors?: Record<string, string[]>;
	serverErrors?: string;
	inputs?: NewChatbot;
	data?: Chatbot;
}
