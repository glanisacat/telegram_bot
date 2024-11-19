import requests

TOKEN = "7755374882:AAFlEOgJhCL49CqZQ2QCdRPvhLEm3iB-JxI"
CHAT_IDS = ["947408005", "634398235"] 
MESSAGE = "Выпей таблетооосиик"

def send_message():
    for chat_id in CHAT_IDS:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": MESSAGE
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"Message sent to {chat_id}!")
        else:
            print(f"Error sending message to {chat_id}: {response.status_code}, {response.text}")

if __name__ == "__main__":
    send_message()
