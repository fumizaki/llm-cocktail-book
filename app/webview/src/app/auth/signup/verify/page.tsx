import { redirect } from "next/navigation";
import { Page, PageHeader, PageTitle } from "@/components/page";
import { verifyAction } from "@/server-actions/auth/signup-verify/action";
import { auth } from "@/auth/config";

export default async function SignupVerify({
	searchParams,
}: {
	searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}) {
	const session = await auth();
	if (session) {
		redirect("/");
	}
	const key = (await searchParams).key;
	await verifyAction(key);

	return (
		<Page>
			<PageHeader>
				<PageTitle title={"Sign Up Verify"} />
			</PageHeader>
		</Page>
	);
}
