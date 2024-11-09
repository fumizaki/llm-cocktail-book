
type StreamTextProps = {
    reader: ReadableStreamDefaultReader<Uint8Array>
    onRead : (value: string) => void 
}

export const readStreamText = async ({reader, onRead}: StreamTextProps) => {
    const decoder = new TextDecoder();
    let done = false;
    let fullText: string = '';
    while (!done) {
        const { done: isDone, value } = await reader.read();
        done = isDone;
        const chunk = decoder.decode(value, { stream: true });
        fullText += chunk;
        onRead(fullText)
    }
}