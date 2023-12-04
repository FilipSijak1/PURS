import requests

payload = {
"temp": 17
}

response = requests.post('http://192.168.86.217:80/temperatura', json=payload)

print(response.text)
print(response.status_code)
