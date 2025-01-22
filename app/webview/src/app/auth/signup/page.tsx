import { redirect } from "next/navigation";
import { Page, PageHeader, PageTitle, PageSection } from "@/components/page";
import { SignupForm } from "@/components/auth/form/signup-form";
import { auth } from "@/auth/config";

export default async function Signup({
	searchParams,
}: {
	searchParams: Promise<{ [key: string]: string | undefined }>;
}) {
	const callbackUrl = (await searchParams).callbackUrl;
	const session = await auth();
	if (session) {
		redirect(callbackUrl ?? "/");
	}
	return (
		<Page>
			<PageHeader>
				<PageTitle title={"Sign Up"} />
			</PageHeader>
			<PageSection id={"signup"}>
				<SignupForm
					callbackUrl={callbackUrl}
					className={"w-full md:max-w-[780px] mx-auto"}
				/>
			</PageSection>
		</Page>
	);
}
