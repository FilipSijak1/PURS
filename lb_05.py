import requests

payload = {
"temperatura": 32
}

response = requests.post('http://192.168.86.212/temperatura',json=payload)

print(response.text)
print(response.status_code)