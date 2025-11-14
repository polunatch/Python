import requests
try:
    response = requests.get("https://httpbin.org/get")
    response.raise_for_status()
    print(response.text)
except requests.exceptions.RequestException as e:
    print("Помилка запиту:", e)
