'use client'

import { useState, useCallback, FormEvent } from 'react';
import { GenerationForm } from '@/components/chatbot/form/generation-form';
import { MessageCardList } from '@/components/chatbot/card/message-card-list';
import { Message } from '@/domain/schema';
import { MessageRole } from '@/domain/value';

export const CodeGeneration = () => {
    const [prompt, setPrompt] = useState('');
    const [messages, setMessages] = useState<Message[]>([]);


    const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        if (!prompt.trim()) return;
        
        // Add user message
        const userMessage: Message = {
            id: Date.now().toString(),
            content: prompt,
            role: MessageRole.USER
        };
        
        setMessages(prev => [...prev, userMessage]);
        setPrompt('');

        try {
            const response = await fetch('/api/generation/txt2code', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const res = await response.json()
            setMessages(prev => [...prev, {
                    id: res.chatbotId,
                    content: res.content,
                    role: res.role
                }])
            

            
        } catch (err) {
            console.error('Failed to fetch chat response:', err);
        } finally {
        }
    }

    return (
        <div className="h-full w-full max-w-3xl mx-auto flex flex-col space-y-4 p-4">
            <div className="flex-1 space-y-4 mb-4">
                <MessageCardList messages={messages}/>
            </div>


            <div className="sticky bottom-0 bg-transparent p-4">
                <GenerationForm
                    prompt={prompt}
                    onChangePrompt={setPrompt}
                    onSubmit={handleSubmit}
                />
            </div>
        </div>
    );
}

