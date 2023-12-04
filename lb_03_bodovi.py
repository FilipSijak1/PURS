import requests

response = requests.post('http://192.168.86.212/svi_bodovi')

print(response.text)
print(response.status_code)