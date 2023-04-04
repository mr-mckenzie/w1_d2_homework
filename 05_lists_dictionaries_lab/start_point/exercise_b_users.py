users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(f'1 - {users["Jonathan"]["twitter"]}')

# 2. Get Erik's hometown
print(f"2 - {users['Erik']['home_town']}")

# 3. Get the list of Erik's lottery numbers
print(f"3 - {users['Erik']['lottery_numbers']}")

# 4. Get the species of Avril's pet Monty
print(f"4 - {users['Avril']['pets'][0]['species']}")

# 5. Get the smallest of Erik's lottery numbers
print(f'5 - {min(users["Erik"]["lottery_numbers"])}')

# 6. Return an list of Avril's lottery numbers that are even
avril_even = []
for lottery_number in users['Avril']['lottery_numbers']:
    if lottery_number % 2 == 0:
        avril_even.append(lottery_number)

print(f"6 - {avril_even}")

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]['lottery_numbers'].append(7)

print(f"7 - {users['Erik']['lottery_numbers']}")

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"

print(f'8 - {users["Erik"]["home_town"]}')

# 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"].append({"name":"fluffy", "species":"dog"})

print(f'9 - {users["Erik"]["pets"][-1]}')

# 10. Add another person to the users dictionary
users["Tim"] = { 
    "twitter" : "tiny_tim",
    "lottery_numbers" : [3, 8, 47, 24, 19, 0],
    "home_town" : "Perth",
    "pets" : [
      {
        "name" : "joan",
        "species" : "narwhal"
      }
    ]
}

print(f"10 - {users['Tim']}")
