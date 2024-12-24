import { CodeGeneration } from "@/components/chatbot/generation/code-generation"

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
                <CodeGeneration/>
            </div>
        </div>
        
    )
}