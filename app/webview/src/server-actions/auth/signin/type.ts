import type { AuthToken } from "@/domain/schema";

export type SigninActionState = {
	success?: boolean;
	message?: string;
	validationErrors?: Record<string, string[]>;
	serverErrors?: string;
	inputs?: { email: string; password: string };
	data?: AuthToken;
};
