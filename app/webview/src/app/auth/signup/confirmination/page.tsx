import { redirect } from "next/navigation";
import { Page, PageHeader, PageTitle, PageSection } from "@/components/page";
import { SignupConfirminationCard } from "@/components/auth/card/signup-confirmination-card";
import { auth } from "@/auth/config";

export default async function SignupConfirmination() {
	const session = await auth();
	if (session) {
		redirect("/");
	}
	return (
		<Page>
			<PageHeader>
				<PageTitle title={"Thank you for Sign up"} />
			</PageHeader>
			<PageSection id={"signup-confirmination"}>
				<SignupConfirminationCard
					className={"w-full md:max-w-[780px] mx-auto"}
				/>
			</PageSection>
		</Page>
	);
}
