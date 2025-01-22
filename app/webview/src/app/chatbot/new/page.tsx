import { Page, PageHeader, PageTitle, PageSection } from "@/components/page";
import { LinkButton } from "@/components/ui/link-button";
import { CreateChatbotForm } from "@/components/chatbot/form/create-chatbot-form";

export default async function NewChatbot() {
	return (
		<Page>
			<PageHeader>
				<PageTitle title={"Chatbot"} />
				<LinkButton href={"/chatbot"}>List</LinkButton>
			</PageHeader>
			<PageSection id={"new-chatbot"}>
				<CreateChatbotForm className={'w-full md:max-w-[780px] mx-auto'}/>
			</PageSection>
		</Page>
	);
}
