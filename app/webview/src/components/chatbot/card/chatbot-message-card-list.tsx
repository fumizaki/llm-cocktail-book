import { AggChatbot } from "@/domain/aggregate";
import { ChatbotMessage } from "@/domain/schema";
import { ChatbotMessageCard } from "@/components/chatbot/card/chatbot-message-card";
import { getAllAction } from "@/server-actions/chatbot-message/get-all"

type Props = {
    chatbotId: string;
};

export async function ChatbotMessageCardList({chatbotId}: Props) {
    const state = await getAllAction(chatbotId)

    if (!state.data) {
        return (
            <div className='flex h-full w-96 mx-auto'>
                <p>データがありません</p>
            </div>
        );
    }

    if (state.data.messages.length <= 0) {
        return (
            <div className='flex h-full w-96 mx-auto'>
                <p>データがありません</p>
            </div>
        );
    }
    return (
        <ul className={'grid grid-cols-1 justify-center items-center gap-x-5 gap-y-8'}>
            {state.data.messages.map((value: ChatbotMessage, idx: number) => {
                return (
                    <li key={idx} className={'w-full group relative flex justify-center items-center '}>
                        <ChatbotMessageCard value={value} />
                    </li>
                );
            })}
        </ul>
    );
}