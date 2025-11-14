import requests
data = {'username': "Kovalenko", "password": "12345"}
response = requests.post("https://httpbin.org/post", data=data)
print(response.text)