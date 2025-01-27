'use client'

import { useState } from "react";
import {
	Dialog,
	DialogContent,
	DialogDescription,
	DialogHeader,
	DialogTitle,
	DialogTrigger,
} from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Pencil } from "lucide-react";
import { ChargeCreditPaymentCheckoutForm } from "@/components/credit/form/charge-credit-payment-checkout-form";
import { ChargeCreditPaymentConfirminationCard } from "@/components/credit/card/charge-credit-payment-confirmination-card";

type Props = {
};

export const ChargeCreditDialog = ({  }: Props) => {
	
	const [clientSecret, setClientSecret] = useState<string | null>(null)
	const handleSuccessChargeCredit = ({ data }: { data?: { clientSecret: string } }) => {
		if (data) {
			setClientSecret(data.clientSecret)
		}
	}
	
	return (
		<Dialog>
			<DialogTrigger asChild>
				<Button size={"icon"} variant={"ghost"}>
					<Pencil />
				</Button>
			</DialogTrigger>
			<DialogContent>
				<DialogHeader>
					<DialogTitle>Confirm Payment</DialogTitle>
				</DialogHeader>
				{clientSecret ? (
					<ChargeCreditPaymentConfirminationCard clientSecret={clientSecret}/>
				):(
					<ChargeCreditPaymentCheckoutForm onSuccess={handleSuccessChargeCredit}/>
				)}
			</DialogContent>
		</Dialog>
	);
};
