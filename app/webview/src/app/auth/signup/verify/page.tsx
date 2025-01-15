import { redirect } from "next/navigation";
import { Page, PageHeader, PageTitle, PageSection } from "@/components/page";
import { verifyAction } from "@/server-actions/auth/signup-verify/action";
import { auth } from "@/auth/config";

export default async function SignupVerify({
	searchParams,
}: {
	searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}) {
	const key = (await searchParams).key;
	const state = await verifyAction(key);
	const session = await auth();
	if (session) {
		redirect("/");
	}

	return (
		<Page>
			<PageHeader>
				<PageTitle title={"Sign Up Verify"} />
			</PageHeader>
			<PageSection id={"signup-verify"}>
				{state.data && <p>{state.data.accessToken}</p>}
			</PageSection>
		</Page>
	);
}
