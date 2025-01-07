'use client'

import { useActionState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { createAction } from '@/server-actions/chatbot-message/create';

type Props = {
    chatbotId: string
}

export const CreateChatbotMessageForm = ({chatbotId}: Props) => {

    const [state, formAction, isPending] = useActionState(createAction, { 
        chatbotId: chatbotId, 
        meta: {
            llm: 'openai',
            mode: 'text',
        },
        prompt: 'build a cv-application',
    })


    return (
        <form action={formAction}>
            {state.validationErrors && (<p>バリデーションエラー</p>)}
            <Input type={'text'} key={state.chatbotId} name='chatbotId' defaultValue={state.chatbotId}/>
            <Input type={'text'} key={state.prompt} name='prompt' defaultValue={state.prompt}/>
            <Input type={'text'} key={state.meta.llm} name='meta.llm' defaultValue={state.meta.llm}/>
            <Input type={'text'} key={state.meta.mode} name='meta.mode' defaultValue={state.meta.mode}/>
            <Button type={'submit'} disabled={isPending}>Send Message</Button>
        </form>
    )
}