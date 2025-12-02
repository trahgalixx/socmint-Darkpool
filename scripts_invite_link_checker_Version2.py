import requests
import time

# Dummy: list of WhatsApp & Telegram invite links
invite_links = [
    'https://chat.whatsapp.com/DUMMYCODE1',
    'https://t.me/joinchat/DUMMYCODE2',
    'https://chat.whatsapp.com/DUMMYCODE3',
    'https://t.me/joinchat/DUMMYCODE4',
]

def check_telegram_link(link):
    try:
        resp = requests.get(link, timeout=8, allow_redirects=True)
        # Telegram returns 200 for valid, 404 for expired
        if resp.status_code == 200 and "Join Channel" in resp.text:
            return True
    except Exception as e:
        pass
    return False

def check_whatsapp_link(link):
    try:
        resp = requests.get(link, timeout=8, allow_redirects=True)
        if resp.status_code == 200 and "WhatsApp" in resp.text:
            return True
    except Exception as e:
        pass
    return False

if __name__ == "__main__":
    for link in invite_links:
        if "t.me" in link or "telegram" in link:
            is_active = check_telegram_link(link)
        elif "whatsapp" in link:
            is_active = check_whatsapp_link(link)
        else:
            is_active = False
        print(f"{link} -> {'ACTIVE' if is_active else 'INACTIVE'}")
        time.sleep(2)  # avoid rate limit