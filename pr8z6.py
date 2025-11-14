import requests
try:
    response = requests.get("https://example.com")
    response.raise_for_status()
    with open("example.html", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("Вміст збережено у example.html")
except requests.exceptions.RequestException as e:
    print("Помилка запиту:", e)
