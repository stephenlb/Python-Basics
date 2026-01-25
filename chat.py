## chat.py
## Simple chat client with basic UX improvements
import communication
import sys
from datetime import datetime

# Colors for terminal
BOLD = '\033[1m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RED = '\033[31m'
CYAN = '\033[36m'
RESET = '\033[0m'

# Store the current username
current_user = ""

def format_time():
    """Return current time as HH:MM"""
    return datetime.now().strftime("%H:%M")

def on_message_received(data):
    """Handle incoming messages"""
    for msg in data[0]:
        # Skip if not a valid message dict
        if not isinstance(msg, dict):
            continue
        
        user = msg.get("user", "")
        text = msg.get("message", "")
        time_str = format_time()
        
        # Skip our own messages (they echo back from PubNub)
        if user == current_user:
            continue
        
        # Format system messages differently
        if "SYSTEM" in user:
            print(f"\n{YELLOW}[{time_str}] ⚡ {text}{RESET}")
        else:
            print(f"\n{CYAN}[{time_str}] ← [{user}]: {text}{RESET}")

# === MAIN PROGRAM ===

channel = 'chat'

# Welcome and get username
print(f"{BOLD}{GREEN}Welcome to Chat!{RESET}")
current_user = input(f"{BLUE}Username: {YELLOW}").strip()

if not current_user:
    current_user = "Anonymous"

print(f"{GREEN}Joined as {current_user}. Type 'logout' to exit.{RESET}\n")

# Fetch and display message history
print(f"{YELLOW}--- Recent Messages ---{RESET}")
history = communication.getHistory(channel, 10)
if history:
    for msg in history:
        if isinstance(msg, dict):
            user = msg.get("user", "Unknown")
            text = msg.get("message", "")
            if "SYSTEM" in user:
                print(f"{YELLOW}⚡ {text}{RESET}")
            else:
                print(f"{CYAN}← [{user}]: {text}{RESET}")
else:
    print(f"{CYAN}No message history yet.{RESET}")
print(f"{YELLOW}--- End of History ---{RESET}\n")

# Start listening for messages
communication.startStream(channel, on_message_received)

# Announce that we joined
join_msg = {"user": "SYSTEM", "message": f"{current_user} has joined"}
communication.send(channel, join_msg)

# Main loop - send messages
while True:
    message = input(f"{BLUE}> {RESET}").strip()
    
    # Skip empty messages
    if not message:
        continue
    
    # Handle logout
    if message.lower() == 'logout':
        leave_msg = {"user": "SYSTEM", "message": f"{current_user} has left"}
        communication.send(channel, leave_msg)
        communication.update_running(False)
        print(f"{GREEN}Goodbye! 👋{RESET}")
        sys.exit()
    
    # Send the message
    payload = {"user": current_user, "message": message}
    communication.send(channel, payload)
    
    # Show our own message with → indicator
    time_str = format_time()
    print(f"{GREEN}[{time_str}] → {message}{RESET}")
