import requests

TOKEN = "7755374882:AAFlEOgJhCL49CqZQ2QCdRPvhLEm3iB-JxI" 
CHAT_ID = "947408005"  # Замените на ваш chat_id
MESSAGE = "Выпей таблетооосееек  "  # Сообщение для отправки

def send_message():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": MESSAGE
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Сообщение отправлено успешно!")
    else:
        print(f"Ошибка: {response.status_code}, {response.text}")

if __name__ == "__main__":
    send_message()
