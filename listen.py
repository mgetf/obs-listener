import asyncio
import websockets
import json

async def handle_websocket(websocket, path):
    try:
        async for message in websocket:
            try:
                # Parse the incoming message as JSON
                data = json.loads(message)
                print("Received JSON:")
                print(json.dumps(data, indent=2))
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
