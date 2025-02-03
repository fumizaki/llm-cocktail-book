"use client";

import { useState } from "react";
import { cn } from "@/lib/style";
import { Button } from "@/components/ui/button";
import {
	Card,
	CardHeader,
	CardTitle,
	CardDescription,
	CardContent,
} from "@/components/ui/card";
import {
	PaymentElement,
	useStripe,
	useElements
} from '@stripe/react-stripe-js';

type Props = {
	className?: string;
}

export const ChargeCreditPaymentConfirminationForm = ({ className }: Props) => {
	
	const stripe = useStripe()
	const elements = useElements()
	
	const [message, setMessage] = useState<string | null>(null);
	const [isLoading, setIsLoading] = useState<boolean>(false);


	const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
		e.preventDefault();

		if (!stripe || !elements) {
			// Stripe.js hasn't yet loaded.
			// Make sure to disable form submission until Stripe.js has loaded.
			return;
		}

		setIsLoading(true);

		const { error } = await stripe.confirmPayment({
			elements,
			confirmParams: {
				// FIXME: Make sure to change this to your payment completion page
				return_url: "http://localhost:3000/credit",
			},
		});

		if (error.type === "card_error" || error.type === "validation_error") {
			setMessage(error.message ?? 'An unexpected error occurred.');
		} else {
			setMessage("An unexpected error occurred.");
		}
	  
		setIsLoading(false);
	}

	return (
		<form
			className={cn(
				`w-full flex flex-col justify-center items-center`,
				className,
			)}
			onSubmit={handleSubmit}
		>
			<Card className={`w-full`}>
				<CardHeader>
					<CardTitle>お支払い</CardTitle>
					<CardDescription>{message}</CardDescription>
				</CardHeader>
				<CardContent className="flex flex-col gap-3">
					<PaymentElement />
					<Button type="submit" disabled={isLoading || !stripe || !elements}>
						Pay
					</Button>
				</CardContent>
			</Card>
		</form>
	)
}