import { useState, useCallback, useRef } from "react";

export const useStreamReader = () => {
	const [data, setData] = useState<string>("");
	const [error, setError] = useState<Error | null>(null);
	const isStreamingRef = useRef(false);

	const handleStream = useCallback(
		async (
			reader: ReadableStreamDefaultReader<Uint8Array>,
			onReadChunk: (chunk: string) => void,
		) => {
			const decoder = new TextDecoder();
			try {
				isStreamingRef.current = true;
				while (isStreamingRef.current) {
					const { done: isDone, value } = await reader.read();
					if (isDone) {
						isStreamingRef.current = false;
						break;
					}
					const chunk = decoder.decode(value, { stream: true });
					setData((prevText) => prevText + chunk);
					onReadChunk(chunk);
				}
			} catch {
				setError(new Error("Failed to Stream"));
			}
		},
		[],
	);

	const stopStreaming = useCallback(() => {
		isStreamingRef.current = false;
	}, []);

	return {
		data,
		error,
		isStreaming: isStreamingRef.current,
		handleStream,
		stopStreaming,
	};
};
