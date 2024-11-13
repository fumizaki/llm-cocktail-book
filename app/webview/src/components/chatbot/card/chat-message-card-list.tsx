import { ChatMessage } from "@/domain/schema";
import { ChatMessageCard } from "@/components/chatbot/card/chat-message-card";

type Props = {
    messages: ChatMessage[]
};

export function ChatMessageCardList({messages}: Props) {
    // TODO: messagesはpropsで受け取らずにbackendから取得する
    // websocketでbackendと繋ぐか
    const values: ChatMessage[] = messages;

    if (values.length <= 0) {
        return (
            <div className='flex h-full w-96 mx-auto'>
                <p>データがありません</p>
            </div>
        );
    }
    return (
        <ul className={'grid grid-cols-1 justify-center items-center gap-x-5 gap-y-8'}>
            {values.map((value: ChatMessage, idx: number) => {
                return (
                    <li key={idx} className={'w-full group relative flex justify-center items-center '}>
                        <ChatMessageCard {...value} />
                    </li>
                );
            })}
        </ul>
    );
}