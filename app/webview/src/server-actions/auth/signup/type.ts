import type { SignUpRequestParams } from "@/domain/schema";

export interface SignupActionState extends SignUpRequestParams {
	validationErrors?: string[] | Record<string, string[]>;
	serverErrors?: string[] | Record<string, string[]>;
}
