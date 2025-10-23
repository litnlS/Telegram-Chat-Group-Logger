# Telegram-Chat-Group-Logger

A small Python script that watches multiple Telegram channels and copies every new message as plain text into another group or channel.  
It uses your Telegram account via **Telethon** and keeps message logs for backup.

---

### Requirements
- Windows 10 or 11  
- Python 3.9 or newer  
- Telegram account  
- API ID and API Hash from [https://my.telegram.org](https://my.telegram.org)

---

### Setup (Windows)

1. **Download or clone this repo**
git clone https://github.com/<your-username>/telegram-multi-channel-copier.git
cd telegram-multi-channel-copier


2. **Install dependencies**
pip install -r req.txt

3. **Edit your details**
Open `multi_channel_copier.py` and fill in:
API_ID = 123456
API_HASH = "your_api_hash_here"
SOURCE_CHANNELS = ["@example1", -1009876543210]
DESTINATION_CHAT = -1001234567890

4. **Run the bot**
python main.py

The first time you run it, it’ll ask for your phone number and Telegram code.  
Your login session will be saved automatically.

---

### Logs
Messages are stored in:
copied_messages.txt

---

### Notes
- Only supports text messages.  
- Do **not** share your `.session` file.  

---

### License
MIT
