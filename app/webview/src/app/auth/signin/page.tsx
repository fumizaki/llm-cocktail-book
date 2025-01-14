import { Page, PageHeader, PageTitle, PageSection } from "@/components/page";
import { SigninForm } from "@/components/auth/form/signin-form";

export default async function Signin({
	searchParams,
}: {
	searchParams: Promise<{ [key: string]: string | undefined }>;
}) {
	const callbackUrl = (await searchParams).callbackUrl
	return (
		<Page>
			<PageHeader>
				<PageTitle title={"Sign in"} />
			</PageHeader>
			<PageSection id={"signin"}>
				<SigninForm callbackUrl={callbackUrl}/>
			</PageSection>
		</Page>
	);
}
