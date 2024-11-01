'use server'

export async function fetchChatAction(prompt: string): Promise<string> {
    const res = await fetch(`http://webapi:8000/chat/openai/stream?prompt=${prompt}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        // body: JSON.stringify({ prompt }),
    });

    if (!res.ok) {
        throw new Error('Error fetching response: ' + res.statusText);
    }

    const reader = res.body?.getReader();
    const decoder = new TextDecoder();
    let done = false;
    let fullResponse = '';

    if (reader) {
        while (!done) {
            const { done: isDone, value } = await reader.read();
            done = isDone;
            const chunk = decoder.decode(value, { stream: true });
            fullResponse += chunk;
        }
    }

    console.log(fullResponse)
    return fullResponse;
}
