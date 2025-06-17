import os
import sys
import django
import requests

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoInternTask.settings")

# Initialize Django
django.setup()

from core.models import TelegramUser

# Get the bot token from environment variables
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# Base URL for Telegram Bot API
URL = f"https://api.telegram.org/bot{TOKEN}/"

def process_update(update):
    """
    Handle incoming Telegram updates:
    - Extracts message details
    - Registers user in database if not already present
    - Sends a welcome or already-registered message
    """
    msg = update.get("message", {})
    chat = msg.get("chat", {})
    username = chat.get("username", "") or ""
    first_name = chat.get("first_name", "")
    telegram_id = chat.get("id")
    text = msg.get("text", "")
    if text == "/start":
        display_name = username if username else first_name
        obj, created = TelegramUser.objects.get_or_create(
            telegram_id=telegram_id,
            defaults={"telegram_username": username}
        )
        if not created :
            if obj.telegram_username != username:
                obj.telegram_username = username
                obj.save()
            requests.post(f"{URL}sendMessage", data={
                    "chat_id": telegram_id, "text": f"Hello {display_name}, you are already registered!"
                })
        else:
            requests.post(f"{URL}sendMessage", data={
            "chat_id": telegram_id, "text": f"Hello {display_name}, you are registered!"
        })

if __name__ == "__main__":
    offset = None
    # Start infinite loop to keep checking for new updates
    while True:
    # Call Telegram API to get updates
        resp = requests.get(f"{URL}getUpdates", params={"offset": offset, "timeout": 30})
        # Loop through all new updates
        for update in resp.json().get("result", []):
            # Update offset so the same message isn’t processed again
            offset = update["update_id"] + 1
            # Handle the update
            process_update(update)
