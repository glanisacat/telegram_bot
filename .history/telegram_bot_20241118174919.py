import schedule
import time
import requests

TOKEN = "7755374882:AAFlEOgJhCL49CqZQ2QCdRPvhLEm3iB-JxI"
CHAT_ID = "947408005"
MESSAGE = "Выпей таблетооосиик"

def send_message():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": MESSAGE
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("!")
    else:
        print(f"Ошибка: {response.status_code}, {response.text}")

schedule.every().day.at("17:20").do(send_message)

if __name__ == "__main__":
    print("Бот запущен и ожидает выполнения задач...")
    while True:
        schedule.run_pending()  
        time.sleep(1)  
