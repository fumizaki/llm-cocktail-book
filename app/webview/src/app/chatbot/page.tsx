import { Page, PageHeader, PageTitle, PageSection } from "@/components/page";
import { Suspense } from "react";
import { ChatbotTemplate } from "@/components/chatbot/template/chatbot-template";

export default function Chatbot() {
	return (
		<Page>
			<PageHeader>
				<PageTitle title={"Chatbot"} />
			</PageHeader>
			<PageSection id={"chatbot"}>
				<Suspense key={"chatbot"} fallback={<p>loading...</p>}>
					<ChatbotTemplate />
				</Suspense>
			</PageSection>
		</Page>
	);
}
