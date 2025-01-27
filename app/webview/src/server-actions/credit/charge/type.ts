import type { ChargeCredit } from "@/domain/schema";

export interface ChargeActionState {
	success?: boolean;
	message?: string;
	validationErrors?: Record<string, string[]>;
	serverErrors?: string;
	inputs?: ChargeCredit;
	data?: { clientSecret: string };
}
