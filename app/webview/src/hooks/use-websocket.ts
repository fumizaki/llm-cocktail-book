import { useCallback, useEffect, useRef, useState } from 'react';

type StreamContent = string | ArrayBuffer | Blob | null

export const useWebSocket = (url: string, accessToken?: string) => {
    const [isConnected, setIsConnected] = useState<boolean>(false);
    const [stream, setStream] = useState<StreamContent>(null);
    const [error, setError] = useState<Error | null>(null);
    const wsRef = useRef<WebSocket | null>(null);

    const handleOpen = useCallback(() => {
        setIsConnected(true);
    }, []);

    const handleClose = useCallback(() => {
        setIsConnected(false);
    }, []);

    const handleMessage = useCallback((e: MessageEvent) => {
        setStream(e.data)
    }, []);

    const handleError = useCallback(() => {
        setIsConnected(false);
    }, []);

    const disconnect = useCallback(() => {
        if (wsRef.current) {
            wsRef.current.close();
            wsRef.current = null;
        }
        setIsConnected(false);
    }, []);


    const connect = useCallback(() => {

        if (wsRef.current) {
            disconnect()
        }

        try {
            // URLにアクセストークンを追加(TODO: localhost:8000を修正)
            const wsUrl = accessToken 
                ? `ws://localhost:8000${url}?header=${encodeURIComponent(accessToken)}` 
                : `ws://localhost:8000${url}`;
            const ws = new WebSocket(wsUrl);
            wsRef.current = ws;
    
            ws.addEventListener('open', handleOpen);
            ws.addEventListener('close', handleClose);
            ws.addEventListener('message', handleMessage);
            ws.addEventListener('error', handleError);
        } catch (err) {
            setError(err as Error)
        }

    }, [url, handleOpen, handleClose, handleMessage, handleError, disconnect]);


    const send = useCallback((content: StreamContent): void => {
        if (content === null) {
            setError(new Error('コンテンツがありません'))
            return
        }
        
        if (wsRef.current?.readyState === WebSocket.OPEN) {
            wsRef.current.send(content);
        } else {
            setError(new Error('WebSocket is not connected'));
        }
    }, []);

    useEffect(() => {
        connect();
        return () => {
            disconnect();
        };
    }, [connect, disconnect]);

    return { isConnected, stream, error, send, websocket: wsRef.current };
};