import requests

TOKEN = "7755374882:AAFlEOgJhCL49CqZQ2QCdRPvhLEm3iB-JxI"
CHAT_ID = "947408005"
MESSAGE = "Выпей таблетооосиик"

def send_message():
    """Отправляет сообщение в Telegram"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": MESSAGE
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Success! Message sent.")
    else:
        print(f"Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    print("Running script...")
    send_message()