# Task 4: Dictionary (INTERVIEW FAVORITE)

# Do:

# Print name
# Add new key "city"
# Update age to 26
# Loop through dictionary and print key-value


user = {
    "name": "Sadish",
    "age": 26
  }

print(user["name"])
user["city"]="Hyderabad"
user.update({"age":27})
# user["age"] = 27 - A bit cleaner

for key,value in user.items():
    print(f"{key}:{value}")


# FYI - Dictionary can't have duplicate keys