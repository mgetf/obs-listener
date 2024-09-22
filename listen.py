import asyncio
import websockets
import json
from collections import defaultdict

# [arena][1|2] = score
scores = defaultdict(lambda: defaultdict(int))
async def handle_websocket(websocket, path):
    try:
        async for message in websocket:
            try:
                # Parse the incoming message as JSON
                data = json.loads(message)
                if data["type"] == "ScoreNotification":
                    scores[data["payload"]["arena"]][1] = data["payload"]["p1Score"]
                    scores[data["payload"]["arena"]][2] = data["payload"]["p2Score"]
                    print(scores)
            except json.JSONDecodeError:
                print(f"Received non-JSON message: {message}")
    except websockets.exceptions.ConnectionClosed:
        print("WebSocket connection closed")

async def main():
    server = await websockets.serve(handle_websocket, "localhost", 8765)
    print("WebSocket server started on ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
