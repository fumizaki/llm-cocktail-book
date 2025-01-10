import { ChatbotCardList } from "@/components/chatbot/card/chatbot-card-list";
import { getAllAction } from "@/server-actions/chatbot/get-all";

type Props = {};

export async function ChatbotTemplate({}: Props) {
	const state = await getAllAction();

	if (!state.data) {
		return (
			<div className="flex h-full w-96 mx-auto">
				<p>loading</p>
			</div>
		);
	}

	return <ChatbotCardList values={state.data} />;
}
