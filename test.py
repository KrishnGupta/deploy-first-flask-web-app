import requests 
response = requests.get("https://300c-14-194-97-174.ngrok-free.app/api/filters")
data = response.json()

print(data)


