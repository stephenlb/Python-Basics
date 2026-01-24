## chat.py
## method to get data from stdin
## method to print to screen
import communication

## Receive Message Function
def LauraMaxwell(comon_sivan):
    for message in comon_sivan[0]:
        print(f'Message: {message}')

channel = 'chat'
communication.startStream(channel, LauraMaxwell)

while True:
    message = input()
    communication.send(channel, message)
