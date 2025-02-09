import { Page, PageHeader, PageTitle, PageSection } from "@/components/page";
import { LinkButton } from "@/components/ui/link-button";
import { CreateChatbotIndexForm } from "@/components/chatbot/form/create-chatbot-index-form";

export default async function NewChatbotIndex({
	params,
}: { params: Promise<{ chatbotId: string }> }) {
	const chatbotId = (await params).chatbotId;
	return (
		<Page>
			<PageHeader>
				<PageTitle title={"Chatbot"} />
				<LinkButton href={`/chatbot/${chatbotId}/index`}>List</LinkButton>
			</PageHeader>
			<PageSection id={"new-chatbot-index"}>
				<CreateChatbotIndexForm chatbotId={chatbotId} className={"w-full md:max-w-[780px] mx-auto"} />
			</PageSection>
		</Page>
	);
}
