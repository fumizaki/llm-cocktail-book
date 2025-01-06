import { ChatbotMessage } from "@/domain/schema";

export type GetAllActionState = {
    ok: boolean;
    status: number;
    errors?: string[] | Record<string, string[]>;
    data?: ChatbotMessage[];
}