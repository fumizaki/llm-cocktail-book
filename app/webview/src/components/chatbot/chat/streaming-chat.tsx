'use client'

import { useState, FormEvent } from 'react';
import { readStreamText } from '@/lib/stream-text';
import { StreamingChatForm } from '@/components/chatbot/form/streaming-chat-form';

interface Message {
    id: string;
    content: string;
    isUser: boolean;
}

export const StreamingChat = () => {
    const [prompt, setPrompt] = useState('');
    const [messages, setMessages] = useState<Message[]>([]);
    const [currentResponse, setCurrentResponse] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        if (!prompt.trim()) return;

        setIsLoading(true);
        setError(null);
        
        // Add user message
        const userMessage: Message = {
            id: Date.now().toString(),
            content: prompt,
            isUser: true
        };
        
        setMessages(prev => [...prev, userMessage]);
        setCurrentResponse('');
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
                let accumulatedResponse = '';
                await readStreamText({
                    reader,
                    onRead: (value: string) => {
                        accumulatedResponse = value; // Accumulate the complete response
                        setCurrentResponse(value);
                    }
                });

                // Add assistant message only after stream is complete
                if (accumulatedResponse) {
                    const assistantMessage: Message = {
                        id: Date.now().toString(),
                        content: accumulatedResponse,
                        isUser: false
                    };
                    setMessages(prev => [...prev, assistantMessage]);
                }
            }
        } catch (err) {
            setError(err instanceof Error ? err.message : '応答の取得に失敗しました');
            console.error('Failed to fetch chat response:', err);
        } finally {
            setIsLoading(false);
            setCurrentResponse('');
        }
  };

  return (
    <div className="w-full max-w-3xl mx-auto flex flex-col space-y-4 p-4">
        <div className="flex-1 space-y-4 mb-4">
            {messages.map((message) => (
                <div
                    key={message.id}
                    className={`p-4 rounded-lg ${
                    message.isUser 
                        ? 'bg-blue-100 ml-auto max-w-[80%]' 
                        : 'bg-gray-100 max-w-[80%]'
                    }`}
                >
                    <p className="whitespace-pre-wrap break-words">{message.content}</p>
                </div>
            ))}
            
            {currentResponse && (
                <div className="bg-gray-100 p-4 rounded-lg max-w-[80%]">
                    <p className="whitespace-pre-wrap break-words">{currentResponse}</p>
                </div>
            )}

        </div>

        <div className="sticky bottom-0 bg-white p-4 border-t">
            <StreamingChatForm
                prompt={prompt}
                onChangePrompt={setPrompt}
                action={handleSubmit}
                //   disabled={isLoading}
            />
        </div>
    </div>
  );
};