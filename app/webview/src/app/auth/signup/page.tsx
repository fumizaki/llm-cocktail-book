import { Page, PageHeader, PageTitle, PageSection } from "@/components/page";
import { SignupForm } from "@/components/auth/form/signup-form";

export default async function Signup({
	searchParams,
}: {
	searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}) {
	return (
		<Page>
			<PageHeader>
				<PageTitle title={"Sign Up"} />
			</PageHeader>
			<PageSection id={"signup"}>
				<SignupForm />
			</PageSection>
		</Page>
	);
}
