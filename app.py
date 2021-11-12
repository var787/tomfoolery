import requests

r = requests.get("https://swapi.dev/api/people")
print(r.status_code)
