import { redirect } from "next/navigation";
import { Page, PageHeader, PageTitle, PageSection } from "@/components/page";
import { SignupForm } from "@/components/auth/form/signup-form";
import { auth } from "@/auth/config";

export default async function SignupConfirmination() {
	const session = await auth();
	if (session) {
		redirect("/");
	}
	return (
		<Page>
			<PageHeader>
				<PageTitle title={"Confirmination"} />
			</PageHeader>
			<PageSection id={"signup-confirmination"}>
				<p>
					ご登録ありがとうございます。認証メールを送信しました。メール内のリンクをクリックして登録を完了してください。
				</p>
			</PageSection>
		</Page>
	);
}
