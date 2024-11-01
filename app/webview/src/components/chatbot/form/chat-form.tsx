'use client'

import { useState, FormEvent } from 'react';
import { Textarea } from '@/components/ui/textarea';
import { Button } from '@/components/ui/button';
import { fetchChatAction } from '@/server-actions/chat-action'


export const ChatForm = () => {
    const [prompt, setPrompt] = useState<string>('');
    const [response, setResponse] = useState<string>('');

    const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        setResponse('');

        try {
            const chatResponse = await fetchChatAction(prompt);
            setResponse(chatResponse);
        } catch (error) {
            console.error('Failed to fetch chat response:', error);
        }
    };

    return (
        <div>
            <h1>Chat with OpenAI</h1>
            <form onSubmit={handleSubmit}>
                <Textarea
                    value={prompt}
                    onChange={(e) => setPrompt(e.target.value)}
                    placeholder="Type your message here..."
                />
                <Button type="submit">Send</Button>
            </form>
            <div>
                <h2>Response:</h2>
                <pre>{response}</pre>
            </div>
        </div>
    );
}