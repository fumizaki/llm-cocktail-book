import { redirect } from "next/navigation";
import { Page, PageHeader, PageTitle, PageSection } from "@/components/page";
import { SigninForm } from "@/components/auth/form/signin-form";
import { auth } from "@/auth/config";

export default async function Signin({
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
				<PageTitle title={"Sign In"} />
			</PageHeader>
			<PageSection id={"signin"}>
				<SigninForm
					callbackUrl={callbackUrl}
					className={"w-full md:max-w-[780px] mx-auto"}
				/>
			</PageSection>
		</Page>
	);
}
