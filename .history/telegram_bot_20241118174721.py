import schedule
import time
import requests

# Конфигурация
TOKEN = "7755374882:AAFlEOgJhCL49CqZQ2QCdRPvhLEm3iB-JxI"
CHAT_ID = "947408005"
MESSAGE = "Выпей таблетооосиик"

# Функция отправки сообщения
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

# Запланировать задачу на каждый день в 18:00
schedule.every().day.at("18:00").do(send_message)

# Основной цикл
if __name__ == "__main__":
    print("Бот запущен и ожидает выполнения задач...")
    while True:
        schedule.run_pending()  # Проверяет, нужно ли выполнить задачу
        time.sleep(1)  # Задержка, чтобы не нагружать процессор