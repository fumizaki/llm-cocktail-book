import type { AuthToken } from "@/domain/schema";

export type VerifyActionState = {
	errors?: string[] | Record<string, string[]>;
	data?: AuthToken;
};
