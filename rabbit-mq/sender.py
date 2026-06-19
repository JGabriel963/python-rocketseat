import requests


def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}

    requests.post(url, data=payload)


token = "8770426181:AAFhX-2xerCXH_lKDqZM-i1MlEcyOD5E7Zw"
chat_id = "-5574961966"
message = "Hello, World"

send_telegram_message(token, chat_id, message)
