import requests

params = {
    "id": 3
}
response = requests.delete('http://192.168.86.212/temperatura', params=params)

print(response.text)
print(response.status_code)