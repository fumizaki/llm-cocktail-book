import type { AuthToken } from "@/domain/schema";

export type RefreshActionState = {
	data: AuthToken;
};
