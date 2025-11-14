import requests
response = requests.get("https://httpbin.org/get")
print("Статус код:", response.status_code)
print("Заголовки:", response.headers)
print("Тіло відповіді:", response.text)
