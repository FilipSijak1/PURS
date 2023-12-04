import requests

params = {
    "id": 202
}

response = requests.get('http://192.168.86.212/hocu_bod', params=params)

print(response.text)
print(response.status_code)

