# Lab5
DnDeezNuts

**PROBLEM:**
requests.exceptions.MissingSchema: Invalid URL '/api/monsters/ankheg': No scheme supplied. Perhaps you meant https:///api/monsters/ankheg?
**SOLVED:**
I was using relative URLS when I should have been including the whole URL with the base. I added a variable to store the base part of the URL.

**PROBLEM:**
Armor class was outputting really odd (Armor Class:[{'type': 'natural', 'value': 13}]) I needed to narrow down what was presented
**SOLVED:**
Added:  armor_class = next((item["value"] for item in monster_data["armor_class"] if item["type"] == "natural"), None)

**PROBLEM:**
A lot of armor classes were showing up as None, meaning there was an issue retrieving it for certain monsters
**SOLVED:**
  Added:
    def extract_armor_class(monster_data):
      armor_classes = monster_data["armor_class"]
      for armor in armor_classes:
          if armor.get("value") is not None:
              return armor["value"]
      return None
  Changed:
    armor_class = next((item["value"] for item in monster_data["armor_class"] if item["type"] == "natural"), None)
    To:
    armor_class = extract_armor_class(monster_data)

**PROBLEM**
Output looked ugly :(
**SOLVED**
Put new lines on each value, and indented the stats under the name of the monster for more clarity






