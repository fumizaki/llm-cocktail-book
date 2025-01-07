import { Chatbot } from "@/domain/schema";
import { NewChatbotCard, ChatbotCard } from "@/components/chatbot/card/chatbot-card";

type Props = {
    values: Chatbot[]
};

export async function ChatbotCardList({values}: Props) {
    
    if (values.length <= 0) {
        return (
            <div className='flex h-full w-96 mx-auto'>
                <p>データがありません</p>
            </div>
        );
    }
    return (
        <ul className={'grid grid-cols-3 justify-center items-center gap-x-5 gap-y-8'}>
            <li className={'w-full group relative flex justify-center items-center '}>
                <NewChatbotCard/>
            </li>
            {values.map((value: Chatbot, idx: number) => {
                return (
                    <li key={idx} className={'w-full group relative flex justify-center items-center '}>
                        <ChatbotCard value={value} />
                    </li>
                );
            })}
        </ul>
    );
}