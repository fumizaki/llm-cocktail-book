import type { SignUpRequestParams } from "@/domain/schema";

export interface SignupActionState {
	success?: boolean;
	message?: string;
	validationErrors?: Record<string, string[]>;
	serverErrors?: string;
	inputs?: SignUpRequestParams;
}
