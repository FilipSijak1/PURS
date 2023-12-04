import requests

payload = {
"ime": 'Filip',
"prezime": 'Šijak',
"ip": '192.168.86.217'
}
response = requests.post('http://192.168.86.212/',
json=payload)

print(response.text)
print(response.status_code)