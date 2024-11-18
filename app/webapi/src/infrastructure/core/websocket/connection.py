from fastapi import WebSocket

# https://fastapi.tiangolo.com/ja/advanced/websockets/#_5

class WebSocketConnectionClient:

    def __init__(self, max_connections: int = 100) -> None:
        self.actives: list[WebSocket] = []
        self.max_connections = max_connections


    async def connect(self, ws: WebSocket) -> bool:
        if len(self.actives) >= self.max_connections:
            await ws.close(code=1008, reason="Too many Connections")
            return False
        
        await ws.accept()
        self.actives.append(ws)
        return True
    

    async def disconnect(self, ws: WebSocket) -> None:
        if ws in self.actives:
            self.actives.remove(ws)

    
    async def send_text(self, ws: WebSocket, text: str) -> None:
        await ws.send_text(text)
        


