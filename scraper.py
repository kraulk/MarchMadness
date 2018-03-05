import requests

url = 'http://espn.com'

r = requests.get(url)

print(r.status_code)

if r.status_code == 200:
    print("Connection accepted")
