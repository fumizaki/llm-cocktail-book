import { Chatbot } from "@/domain/schema";
import { ChatbotCard } from "@/components/chatbot/card/chatbot-card";
import { getAllAction } from "@/server-actions/chatbot/get-all"

type Props = {
};

export async function ChatbotCardList({}: Props) {
    
    const state = await getAllAction()

    if (!state.data) {
        return (
            <div className='flex h-full w-96 mx-auto'>
                <p>データがありません</p>
            </div>
        );
    }
    
    if (state.data.length <= 0) {
        return (
            <div className='flex h-full w-96 mx-auto'>
                <p>データがありません</p>
            </div>
        );
    }
    return (
        <ul className={'grid grid-cols-1 justify-center items-center gap-x-5 gap-y-8'}>
            {state.data.map((value: Chatbot, idx: number) => {
                return (
                    <li key={idx} className={'w-full group relative flex justify-center items-center '}>
                        <ChatbotCard value={value} />
                    </li>
                );
            })}
        </ul>
    );
}