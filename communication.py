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

# Track active streams per channel
active_streams = {}

## update running flag
def update_running(value: bool):
    global running
    running = value

## Connect To a Channel
def stream(channel: str, callback):
    tt = '0'
    while running and channel in active_streams:
        receive_url = f'https://ps.pndsn.com/subscribe/{subscribeKey}/{channel}/0/{tt}'
        try:
            response = requests.get(receive_url)
            data = response.json()
            tt = data[1]
            # Pass channel info along with data
            callback(channel, data)
        except Exception as e:
            print(e)
            continue
        finally:
            time.sleep(0.1)

def startStream(channel: str, callback):
    """Start a stream for a channel"""
    if channel in active_streams:
        return active_streams[channel]  # Already streaming
    
    thread = threading.Thread(
        target=stream,
        args=(channel, callback)
    )
    # Add to active_streams BEFORE starting thread (fixes race condition)
    active_streams[channel] = thread
    thread.start()
    return thread

def stopStream(channel: str):
    """Stop streaming a specific channel"""
    if channel in active_streams:
        del active_streams[channel]
        return True
    return False

def getActiveChannels():
    """Return list of active channels"""
    return list(active_streams.keys())

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
