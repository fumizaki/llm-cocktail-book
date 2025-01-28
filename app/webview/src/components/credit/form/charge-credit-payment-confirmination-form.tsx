"use client";

import { cn } from "@/lib/style";
import { Button } from "@/components/ui/button";
import {
	Card,
	CardHeader,
	CardTitle,
	CardDescription,
	CardContent,
} from "@/components/ui/card";
import { PaymentElement } from '@stripe/react-stripe-js';

type Props = {
	className?: string;
}

export const ChargeCreditPaymentConfirminationForm = ({ className }: Props) => {
	return (
		<form
			className={cn(
			`w-full flex flex-col justify-center items-center`,
			className,
		)}
		>
			<Card className={`w-full`}>
				<CardHeader>
					<CardTitle>お支払い</CardTitle>
					<CardDescription></CardDescription>
				</CardHeader>
				<CardContent className="flex flex-col gap-3">
					<PaymentElement />
					<Button type="submit">
						Pay
					</Button>
				</CardContent>
			</Card>
		</form>
	)
}