# If Else Condition

x = 29

if x < 30:
    print("Inside If Block")
elif x > 35:
    print("In elif block")
else:
    print("In else block")

print("Outside if-else block")  

# Simple Program to check if a skill is available in a team

DevOps_Team = ["Jenkins","Docker","Azure"]
Dev_Team = ["NodeJs","Salesforce","Python"]

contract_1 = {"name":"Vishal", "Skill":"AI"}
contract_2 = {"name":"Amir", "Skill":"ML"}

check_skill = input("Enter the skill you want to check : ")

if check_skill in DevOps_Team:
    print(f"The skill {check_skill} is present in our DevOps Team")
elif check_skill in Dev_Team:
    print(f"The skill {check_skill} is present in our Dev Team")
elif check_skill in contract_1.values() or check_skill in contract_2.values():   # .values() will also take their names as values so not ideal
    print(f"The skill {check_skill} is present with our contract workers")
else:
    print("Sorry!! No such skill present in our team.")


