import requests

req = requests.get("https://swapi.dev/api/people/2/")
person = req.json()
print(f"Name is\t\t\t{person['name']}")
print(f"Birth year is\t\t{person['birth_year']}")

print("Films involved in:")
for film in person['films']:
    req = requests.get(film)
    film = req.json()
    print("Film is: ", film['title'])
