'use client'

import { useState, useCallback, FormEvent } from 'react';
import { useStreamReader } from "@/hooks/use-stream-reader"
import { StreamingChatForm } from '@/components/chatbot/form/streaming-chat-form';
import { ChatMessageCardList } from '@/components/chatbot/card/chat-message-card-list';
import { StreamingMessageCard } from '@/components/chatbot/card/streaming-message-card';
import { ChatMessage } from '@/domain/schema';
import { ChatRole } from '@/domain/value';

export const StreamingChat = () => {
    const [prompt, setPrompt] = useState('');
    const [messages, setMessages] = useState<ChatMessage[]>([]);
    const { data, isStreaming, handleStream } = useStreamReader();

    const renderStreaming = useCallback(() => {
        return (
            <StreamingMessageCard message={data}/>
        )
    }, [data])

    const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        if (!prompt.trim()) return;
        
        // Add user message
        const userMessage: ChatMessage = {
            id: Date.now().toString(),
            content: prompt,
            role: ChatRole.USER
        };
        
        setMessages(prev => [...prev, userMessage]);
        setPrompt('');

        try {
            const response = await fetch('/api/chat/stream', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const reader = response.body?.getReader();
            if (reader) {
                let text = ''
                await handleStream(reader, (chunk: string) => {text = text + chunk})
                // Add assistant message only after stream is complete
                const assistantMessage: ChatMessage = {
                    id: Date.now().toString(),
                    content: text,
                    role: ChatRole.ASSISTANT
                };
                setMessages(prev => [...prev, assistantMessage]);
            }
        } catch (err) {
            console.error('Failed to fetch chat response:', err);
        } finally {
        }
    }

    return (
        <div className="w-full max-w-3xl mx-auto flex flex-col space-y-4 p-4">
            <div className="flex-1 space-y-4 mb-4">
                <ChatMessageCardList messages={messages}/>
            </div>

            {isStreaming && renderStreaming()}

            <div className="sticky bottom-0 bg-transparent p-4">
                <StreamingChatForm
                    prompt={prompt}
                    onChangePrompt={setPrompt}
                    onSubmit={handleSubmit}
                />
            </div>
        </div>
    );
}

