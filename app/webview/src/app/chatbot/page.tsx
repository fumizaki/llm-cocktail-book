import { Page, PageHeader, PageTitle, PageSection } from "@/components/page";
import { LinkButton } from "@/components/ui/link-button";
import { Suspense } from "react";
import { ChatbotCardList } from "@/components/chatbot/card/chatbot-card-list";

export default async function Chatbot() {
	return (
		<Page>
			<PageHeader>
				<PageTitle title={"Chatbot"} />
				<LinkButton href={"/chatbot/new"}>Create</LinkButton>
			</PageHeader>
			<PageSection id={"chatbot"}>
				<Suspense key={"chatbot"} fallback={<p>loading...</p>}>
					<ChatbotCardList />
				</Suspense>
			</PageSection>
		</Page>
	);
}
