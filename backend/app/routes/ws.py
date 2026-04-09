from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import asyncio

router = APIRouter()

@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()
    try:
        while True:
            try:
                data = await asyncio.wait_for(websocket.receive_text(), timeout=25.0)
                if data == "ping":
                    await websocket.send_text("pong")
                else:
                    await websocket.send_text(f"echo: {data}")
            except asyncio.TimeoutError:
                await websocket.send_text("ping")
    except WebSocketDisconnect:
        pass
