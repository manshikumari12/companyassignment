

import asyncio
import websockets
from data_processing import process_data

async def connect_to_websocket():
    url = "wss://functionup.fintarget.in/ws?id=fintarget-functionup"

    async with websockets.connect(url) as websocket:
        while True:
            data = await websocket.recv()
            process_data(data)

if __name__ == "__main__":
    asyncio.run(connect_to_websocket())

