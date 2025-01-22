import { Page, PageHeader, PageTitle, PageSection, PageLoading } from "@/components/page";
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
				<Suspense key={"chatbot"} fallback={<PageLoading className={'h-80'}/>}>
					<ChatbotCardList className={'w-full md:max-w-[780px] mx-auto'}/>
				</Suspense>
			</PageSection>
		</Page>
	);
}
