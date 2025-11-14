import requests
params = {'q': 'Python', 'page': 1}
response = requests.get("https://httpbin.org/get", params=params)
print(response.text)
