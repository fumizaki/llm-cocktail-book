import Link from "next/link";
import { Page, PageHeader, PageTitle, PageSection } from "@/components/page";
import { Suspense } from "react";
import { CreateChatbotForm } from "@/components/chatbot/form/create-chatbot-form";

export default function NewChatbot() {
	return (
		<Page>
			<PageHeader>
				<PageTitle title={"Chatbot"} />
				<Link href={'/chatbot'}>List</Link>
			</PageHeader>
			<PageSection id={"new-chatbot"}>
				<Suspense key={"new-chatbot"} fallback={<p>loading...</p>}>
					<CreateChatbotForm />
				</Suspense>
			</PageSection>
		</Page>
	);
}
