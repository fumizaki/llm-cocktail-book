import { Page, PageHeader, PageTitle, PageSection } from "@/components/page";
import { LinkButton } from "@/components/ui/link-button";
import { Suspense } from "react";
import { ChatbotMessageCardList } from "@/components/chatbot/card/chatbot-message-card-list";
import { CreateChatbotMessageForm } from "@/components/chatbot/form/create-chatbot-message-form";

export default async function ChatbotMessage({
	params,
}: { params: Promise<{ chatbotId: string }> }) {
	const chatbotId = (await params).chatbotId;

	return (
		<Page>
			<PageHeader>
				<PageTitle title={"Chatbot"} />
				<LinkButton href={"/chatbot"}>List</LinkButton>
			</PageHeader>
			<PageSection id={"chatbot-message"}>
				<Suspense fallback={<p>loading...</p>}>
					<ChatbotMessageCardList chatbotId={chatbotId} />
				</Suspense>
				<CreateChatbotMessageForm chatbotId={chatbotId} />
			</PageSection>
		</Page>
	);
}
