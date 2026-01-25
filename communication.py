## communication.py module
## receive messages and send messages
## threading with ability to start thread using a function callback

import time
import json
import requests
import threading
from urllib.parse import quote

publishKey = 'demo'
subscribeKey = 'demo'

# flag to help with graceful shutdown
running = True

## update running flag
def update_running(value: bool):
    global running
    running = value

## Connect To a Channel
def stream(channel: str, callback):
    tt = '0'
    while running:
        receive_url = f'https://ps.pndsn.com/subscribe/{subscribeKey}/{channel}/0/{tt}'
        try:
            response = requests.get(receive_url)
            data = response.json()
            tt = data[1]
            callback(data)
        except Exception as e:
            print(e)
            continue
        finally:
            time.sleep(0.1)

def startStream(channel: str, callback):
    thread = threading.Thread(
        target=stream,
        args=(channel, callback)
    )
    thread.start()
    return thread

def send(channel: str, payload: dict):
    encoded_payload = quote(json.dumps(payload), safe='')
    send_url = f'https://ps.pndsn.com/publish/{publishKey}/{subscribeKey}/0/{channel}/0/{encoded_payload}'
    try:
        response = requests.get(send_url)
        return response.json()
    except Exception as e:
        print(e)
        return None

def getHistory(channel: str, count: int = 10):
    """Fetch recent messages from a channel"""
    history_url = f'https://ps.pndsn.com/v2/history/sub-key/{subscribeKey}/channel/{channel}?count={count}'
    try:
        response = requests.get(history_url)
        data = response.json()
        # Messages are in data[0]
        return data[0] if data else []
    except Exception as e:
        print(e)
        return []
        
## Test for the module
if __name__ == '__main__':
    channel = 'chat'
    startStream(channel, callback=lambda m: print(m))
    while True:
        print(send(channel, "hello!!!"))
        time.sleep(1)
