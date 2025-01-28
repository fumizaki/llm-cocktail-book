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
import { OrderedCredit } from "@/domain/schema";
import { ChargeCreditPaymentCheckoutForm } from "@/components/credit/form/charge-credit-payment-checkout-form";
import { ChargeCreditPaymentConfirminationCard } from "@/components/credit/card/charge-credit-payment-confirmination-card";

type Props = {
};

export const ChargeCreditDialog = ({  }: Props) => {
	
	const [value, setValue] = useState<OrderedCredit | null>(null)
	const handleSuccessChargeCredit = ({ data }: { data?: OrderedCredit }) => {
		if (data) {
			setValue(data)
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
				{value ? (
					<ChargeCreditPaymentConfirminationCard value={value}/>
				):(
					<ChargeCreditPaymentCheckoutForm onSuccess={handleSuccessChargeCredit}/>
				)}
			</DialogContent>
		</Dialog>
	);
};
