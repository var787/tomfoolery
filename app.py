import requests

# print(sys.version)
 print(sys.executable)


def greet(who_to_greet):
    greeting = f"Hello, {who_to_greet}"
    return greeting


print(greet("Rakshan"))

r = requests.get("https://swapi.dev/api/people")
print(r.status_code)
