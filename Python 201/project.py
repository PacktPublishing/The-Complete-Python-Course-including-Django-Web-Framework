# 1. Ask for user input -> ditto
# 2. Create a dynamic URL based on step 1
# 3. Fetch the data from the url in step 2
# 4. Convert JSON to a dictionary
# 5. Print out pokemon data
import requests

while True:
    pokemon = input("Which pokemon do you want to find? ")
    pokemon = pokemon.lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
        print(f"Name is\t\t{data['name']}")
        print("Abilities:")
        for ability in data['abilities']:
            print(ability['ability']['name'])
    else:
        print("Pokemon not found")

