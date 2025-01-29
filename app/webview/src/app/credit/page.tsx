import { Suspense } from "react";
import {
	Page,
	PageHeader,
	PageTitle,
	PageSection,
	PageLoading,
} from "@/components/page";
import { LinkButton } from "@/components/ui/link-button";
import { CreditBalanceCard } from "@/components/credit/card/credit-balance-card";


export default function CreditCharge() {

	return (
		<Page>
			<PageHeader>
				<PageTitle title={"Credit"} />
			</PageHeader>
			<PageSection id={"credit"} >
				<Suspense key={"credit"} fallback={<PageLoading className={"h-80"} />}>
					<CreditBalanceCard className={"w-full md:max-w-[780px] mx-auto"}/>
				</Suspense>
			</PageSection>
		</Page>
	);
}
