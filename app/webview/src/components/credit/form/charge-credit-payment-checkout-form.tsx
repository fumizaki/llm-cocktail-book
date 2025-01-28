"use client";

import { cn } from "@/lib/style";
import { useActionState, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
	Card,
	CardHeader,
	CardTitle,
	CardContent,
} from "@/components/ui/card";
import { chargeAction } from "@/server-actions/credit/charge";
import type { ChargeCredit, OrderedCredit } from "@/domain/schema";

type Props = {
	className?: string;
	onSuccess?: ({ data }: { data?: OrderedCredit }) => void
	onFailure?: ({ inputs, message }: { inputs?: ChargeCredit,  message?: string }) => void
};

export const ChargeCreditPaymentCheckoutForm = ({ className, onSuccess, onFailure }: Props) => {

	const [state, formAction, isPending] = useActionState(chargeAction, {
		inputs: {
			amount: 1000,
			currency: 'jpy'
		},
	});

	useEffect(() => {
		if (state.success) {
			onSuccess?.({ data: state.data })
		} else if (state.success === false) {
			onFailure?.({ inputs: state.inputs, message: state.message})
		}
	}, [state]);

	return (
		<form
			action={formAction}
			className={cn(
				`w-full flex flex-col justify-center items-center`,
				className,
			)}
		>
			<Card className={`w-full`}>
				<CardHeader>
					<CardTitle>Cherge Credit</CardTitle>
				</CardHeader>
				<CardContent className="flex flex-col gap-3">
					<Label className={'flex flex-col gap-1.5'}>
						Amount to charge
						<Input
							type={"number"}
							name={"inputs.amount"}
							defaultValue={state.inputs?.amount}
							className={state.validationErrors?.amount && "bg-red-200"}
						/>
						{state.validationErrors?.amount && (
							<small>{state.validationErrors?.amount}</small>
						)}
					</Label>
					<Input
						type={"hidden"}
						key={state.inputs?.currency}
						name={"inputs.currency"}
						defaultValue={state.inputs?.currency}
					/>
					<Button type="submit" disabled={isPending}>
						Continue
					</Button>
				</CardContent>
			</Card>
		</form>
	);
};
