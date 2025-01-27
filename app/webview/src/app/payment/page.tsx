import {
	Page,
	PageHeader,
	PageTitle,
	PageSection,
	PageLoading,
} from "@/components/page";
import { LinkButton } from "@/components/ui/link-button";
import { Suspense } from "react";
import { StripeCheckoutCard } from "@/components/payment/card/stripe-checkout-card";

export default async function Payment() {
	return (
		<Page>
			<PageHeader>
				<PageTitle title={"Payment"} />
				<LinkButton href={"#"}>Create</LinkButton>
			</PageHeader>
			<PageSection id={"payment"}>
				<Suspense key={"payment"} fallback={<PageLoading className={"h-80"} />}>
					<StripeCheckoutCard clientSecret=""/>
				</Suspense>
			</PageSection>
		</Page>
	);
}
