import { Page, PageHeader, PageTitle, PageSection } from "@/components/page";
import { Suspense } from "react";
import { ChatbotMessageTemplate } from "@/components/chatbot/template/chatbot-message-template";

export default async function ChatbotMessage({
	params,
}: { params: Promise<{ chatbotId: string }> }) {
	const chatbotId = (await params).chatbotId;
	return (
		<Page>
			<PageHeader>
				<PageTitle title={"Chatbot"} />
			</PageHeader>
			<PageSection id={"chatbot-message"}>
				<Suspense key={"chatbot-message"} fallback={<p>loading...</p>}>
					<ChatbotMessageTemplate chatbotId={chatbotId} />
				</Suspense>
			</PageSection>
		</Page>
	);
}
