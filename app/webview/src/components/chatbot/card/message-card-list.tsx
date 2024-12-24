import { Message } from "@/domain/schema";
import { MessageCard } from "@/components/chatbot/card/message-card";

type Props = {
    messages: Message[]
};

export function MessageCardList({messages}: Props) {
    const values: Message[] = messages;

    if (values.length <= 0) {
        return (
            <div className='flex h-full w-96 mx-auto'>
                <p>データがありません</p>
            </div>
        );
    }
    return (
        <ul className={'grid grid-cols-1 justify-center items-center gap-x-5 gap-y-8'}>
            {values.map((value: Message, idx: number) => {
                return (
                    <li key={idx} className={'w-full group relative flex justify-center items-center '}>
                        <MessageCard {...value} />
                    </li>
                );
            })}
        </ul>
    );
}