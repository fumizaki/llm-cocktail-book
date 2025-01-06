import { AggChatbot } from "@/domain/aggregate";

export type GetAllActionState = {
    ok: boolean;
    status: number;
    errors?: string[] | Record<string, string[]>;
    data?: AggChatbot;
}