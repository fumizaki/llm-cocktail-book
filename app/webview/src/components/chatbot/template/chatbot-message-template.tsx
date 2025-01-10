import { getAllAction } from "@/server-actions/chatbot-message/get-all";
import { ChatbotMessageCardList } from "@/components/chatbot/card/chatbot-message-card-list";
import { CreateChatbotMessageForm } from "@/components/chatbot/form/create-chatbot-message-form";

type Props = {
	chatbotId: string;
};

export async function ChatbotMessageTemplate({ chatbotId }: Props) {
	const state = await getAllAction(chatbotId);

	if (!state.data) {
		return (
			<div className="flex h-full w-96 mx-auto">
				<p>loading</p>
			</div>
		);
	}

	return (
		<div className={"flex flex-col gap-3"}>
			<p>{state.data.title}</p>
			<ChatbotMessageCardList values={state.data.messages} />
			<CreateChatbotMessageForm chatbotId={chatbotId} />
		</div>
	);
}
