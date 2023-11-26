
import websocket
import json
from data import process_data

WEBSOCKET_URL = "wss://functionup.fintarget.in/ws?id=fintarget-functionup"

def on_message(ws, message):
    data = json.loads(message)
    process_data(data)

def connect_to_websocket():
    ws = websocket.WebSocketApp(WEBSOCKET_URL, on_message=on_message)
    ws.run_forever()

if __name__ == "__main__":
    connect_to_websocket()

