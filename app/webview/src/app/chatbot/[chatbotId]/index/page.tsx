import {
	Page,
	PageHeader,
	PageTitle,
	PageSection,
	PageLoading,
} from "@/components/page";
import { LinkButton } from "@/components/ui/link-button";
import { Suspense } from "react";
import { ChatbotIndexCardList } from "@/components/chatbot/card/chatbot-index-card-list";

export default async function ChatbotIndex({
	params,
}: { params: Promise<{ chatbotId: string }> }) {
	const chatbotId = (await params).chatbotId;

	return (
		<Page>
			<PageHeader>
				<PageTitle title={"Chatbot"} />
				<LinkButton href={`/chatbot/${chatbotId}/index/new`}>New</LinkButton>
			</PageHeader>
			<PageSection id={"chatbot-index"}>
				<Suspense fallback={<PageLoading className={"h-80"} />}>
					<ChatbotIndexCardList chatbotId={chatbotId} className={"w-full md:max-w-[780px] mx-auto"}/>
				</Suspense>
			</PageSection>
		</Page>
	);
}
