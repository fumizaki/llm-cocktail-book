import { ChatbotMessage } from "@/domain/schema";
import { ChatbotMessageCard } from "@/components/chatbot/card/chatbot-message-card";

type Props = {
    values: ChatbotMessage[]
};

export async function ChatbotMessageCardList({values}: Props) {
    

    if (values.length <= 0) {
        return (
            <div className='flex h-full w-96 mx-auto'>
                <p>データがありません</p>
            </div>
        );
    }
    
    return (
        <ul className={'grid grid-cols-1 justify-center items-center gap-x-5 gap-y-8'}>
            {values.map((value: ChatbotMessage, idx: number) => {
                return (
                    <li key={idx} className={'w-full group relative flex justify-center items-center '}>
                        <ChatbotMessageCard value={value} />
                    </li>
                );
            })}
        </ul>
    );
}