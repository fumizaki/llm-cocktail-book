import type { AuthToken } from "@/domain/schema";

export type RefreshActionState = {
	ok: boolean;
	status: number;
	errors?: string[] | Record<string, string[]>;
	data?: AuthToken;
};
