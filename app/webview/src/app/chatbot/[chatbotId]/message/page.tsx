import { Page, PageHeader, PageTitle, PageSection } from "@/components/page";
import { LinkButton } from "@/components/ui/link-button";
import { Suspense } from "react";
import { getAllAction } from "@/server-actions/chatbot-message/get-all";
import { ChatbotMessageCardList } from "@/components/chatbot/card/chatbot-message-card-list";
import { CreateChatbotMessageForm } from "@/components/chatbot/form/create-chatbot-message-form";

export default async function ChatbotMessage({
	params,
}: { params: Promise<{ chatbotId: string }> }) {
	const chatbotId = (await params).chatbotId;
	const state = await getAllAction(chatbotId);

	return (
		<Page>
			<PageHeader>
				<PageTitle title={state.data.title} />
				<LinkButton href={'/chatbot'}>List</LinkButton>
			</PageHeader>
			<PageSection id={"chatbot-message"}>
				<Suspense key={"chatbot-message"} fallback={<p>loading...</p>}>
					<ChatbotMessageCardList values={state.data.messages} />
				</Suspense>
				<CreateChatbotMessageForm chatbotId={chatbotId} />
			</PageSection>
		</Page>
	);
}
