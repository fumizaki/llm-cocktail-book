import type * as schema from "@/domain/schema";

export type AggChatbot = schema.Chatbot & { messages: schema.ChatbotMessage[] };
