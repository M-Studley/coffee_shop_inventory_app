import requests

r = requests.get('http://127.0.0.1:5000/stores')
raw_data = r.json()

for item in raw_data:
    for key, value in item.items():
        print(f"{key}: {value}")
