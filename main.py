from telethon import TelegramClient, events
from datetime import datetime
import asyncio
import os

# ========== SETTINGS ==========
API_ID = 1234567                        # Replace with your API_ID | https://my.telegram.org/
API_HASH = "your_api_hash_here"         # Replace with your API_HASH
SOURCE_CHANNEL = -10001000000         # Channel ID (use @username or numeric ID)
DESTINATION_CHAT = -10001000000       # Group/Channel ID to forward messages to
LOG_FILE = "forwarded_messages.log"     # Log file name
SESSION_NAME = "forwarder_session"      # Saved session file name
# ===============================

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

if not os.path.exists(LOG_FILE):
    open(LOG_FILE, "w").close()

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def forward_message(event):
    try:
        await event.forward_to(DESTINATION_CHAT)
        
        message_text = event.message.message or ""
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message_text}\n")
        
        print(f"Forwarded and logged message: {message_text[:50]}")

    except Exception as e:
        print(f"Error forwarding message: {e}")

async def main():
    print("Starting Telegram forwarding bot...")
    await client.start()
    print("Logged in successfully. Monitoring started...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
