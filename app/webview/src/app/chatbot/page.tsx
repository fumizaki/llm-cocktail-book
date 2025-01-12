import { Page, PageHeader, PageTitle, PageSection } from "@/components/page";
import { Suspense } from "react";
import { ChatbotCardList } from "@/components/chatbot/card/chatbot-card-list";
import { getAllAction } from "@/server-actions/chatbot/get-all";

export default async function Chatbot() {
	const state = await getAllAction();

	return (
		<Page>
			<PageHeader>
				<PageTitle title={"Chatbot"} />
			</PageHeader>
			<PageSection id={"chatbot"}>
				<Suspense key={"chatbot"} fallback={<p>loading...</p>}>
					<ChatbotCardList values={state.data} />
				</Suspense>
			</PageSection>
		</Page>
	);
}
