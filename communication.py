## communication.py module
## receive messages and send messages
## threading with ability to start thread using a function callback

import time
import json
import requests
import threading

publishKey = 'demo'
subscribeKey = 'demo'

## Connect To a Channel
def stream(channel: str, callback):
    tt = '0'
    while True:
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

def send(channel: str, message: str):
    send_url = f'https://ps.pndsn.com/publish/{publishKey}/{subscribeKey}/0/{channel}/0/{json.dumps(message)}'
    try:
        response = requests.get(send_url)
        return response.json()
    except Exception as e:
        print(e)
        return None
        
## Test for the module
if __name__ == '__main__':
    channel = 'chat'
    startStream(channel, callback=lambda m: print(m))
    while True:
        print(send(channel, "hello!!!"))
        time.sleep(1)
