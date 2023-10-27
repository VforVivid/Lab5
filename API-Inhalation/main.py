import requests
import random

BASE_URL = "https://www.dnd5eapi.co"

#gets information about monsters from the DnD 5e API based on # the provided challenge rating.
def monsterChal(challenge_rating):
    url = f"{BASE_URL}/api/monsters/?challenge_rating={challenge_rating}"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()["results"]
        monsters = []
        for result in results:
            monster_url = BASE_URL + result["url"]
            monster_response = requests.get(monster_url)
            if monster_response.status_code == 200:
                monster_data = monster_response.json()
                armor_class = armorClass(monster_data)
                monsters.append({
                    "name": monster_data["name"],
                    "size": monster_data["size"],
                    "type": monster_data["type"],
                    "armor_class": armor_class
                })
        return monsters
    else:
        return None

#gets the armor class of the monster
def armorClass(monster_data):
    armor_classes = monster_data["armor_class"]
    for armor in armor_classes:
        if armor.get("value") is not None:
            return armor["value"]
    return None

#selects a monster randomly
def randoMonster(challenge_rating, quantity):
    monsters = monsterChal(challenge_rating)
    if monsters:
        selected_monsters = random.sample(monsters, min(quantity, len(monsters)))
        return selected_monsters
    else:
        return None


#takes in user input, also where the information is synthesized and displayed to the user. 
#The "Driver" where we run the functions we made earlier.
if __name__ == "__main__":
    challenge_rating = float(input("Enter the challenge rating: "))
    quantity = int(input("Enter the number of monsters: "))

    selected_monsters = randoMonster(challenge_rating, quantity)

    if selected_monsters:
        print(f"Randomly selected {len(selected_monsters)} monsters with challenge rating {challenge_rating}:")
        for monster in selected_monsters:
            print(f"Name: {monster['name']}")
            print(f"  Size: {monster['size']}")
            print(f"  Type: {monster['type']}")
            print(f"  Armor Class: {monster['armor_class']}\n")
    else:
        print("Failed to retrieve monsters. Please check your input.")
