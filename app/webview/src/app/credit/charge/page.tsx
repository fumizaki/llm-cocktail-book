'use client'

import { useState } from "react";
import {
	Page,
	PageHeader,
	PageTitle,
	PageSection,
	PageLoading,
} from "@/components/page";
import { LinkButton } from "@/components/ui/link-button";
import { ChargeCreditDialog } from "@/components/credit/dialog/charge-credit-dialog";


export default function CreditCharge() {
	const [clientSecret, setClientSecret] = useState<string | null>(null)
	const handleSuccessChargeCredit = ({ data }: { data?: { clientSecret: string } }) => {
		if (data) {
			setClientSecret(data.clientSecret)
		}
	}

	return (
		<Page>
			<PageHeader>
				<PageTitle title={"Credit"} />
				<LinkButton href={"#"}>Create</LinkButton>
			</PageHeader>
			<PageSection id={"credit-charge"} >
				<ChargeCreditDialog/>
			</PageSection>
		</Page>
	);
}
