import { cn } from "@/lib/style";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Coins } from "lucide-react";
import { getAction } from "@/server-actions/credit/get";
import { ChargeCreditDialog } from "@/components/credit/dialog/charge-credit-dialog";

type Props = {
	className?: string;
};

export async function CreditBalanceCard({ className }: Props) {
	
    const state = await getAction();

    return (
		<Card
			className={
				cn("relative w-full", className)
			}
		>
			<CardHeader>
				<CardTitle>Pay as you go</CardTitle>
			</CardHeader>
			<CardContent>
				<p>Credit balance</p>
				<div className={'w-full flex justify-between p-2'}>
					<div className={'flex gap-3 items-center'}>
						<Coins/><p className={'text-xl'}>{state.data.balance}</p>
					</div>
					<ChargeCreditDialog/>
				</div>
			</CardContent>
		</Card>
	);
};
