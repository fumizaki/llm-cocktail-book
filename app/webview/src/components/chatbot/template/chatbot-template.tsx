import { useState } from "react"
import { StreamingChat } from "@/components/chatbot/chat/streaming-chat"

type Props = {

}

export const ChatbotTemplate = ({

}: Props) => {
    return (
        <div className={'w-full flex flex-col justify-between'}>
            <div>
                <p>CHATBOT</p>
            </div>
            <div className={'w-full'}>
                <StreamingChat/>
            </div>
        </div>
        
    )
}