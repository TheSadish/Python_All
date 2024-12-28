'''
Break and Continue
Print the planets till you find a character z

'''

planet = ["Mercury","Venus","Ezarth","Mars"]

i = 0
for plan in planet:
    if "z" in plan:
        break
    else:
        print(planet[i])
        i+=1

# Skip the planet if you find an z there
        
i = 0
for plan in planet:
    if "z" in plan:
        i+=1
        continue
    else:
        print(planet[i])
        i+=1


# From a list of name, shuffle it, get a lucky name using random and find its spot in the main list
import random

mylist = ["Sadish","Sidhant","Sumit","Saurabh","Gaurav"]

mylist_random = mylist
random.shuffle(mylist_random)
# print(mylist_random)

lucky_name = random.choice(mylist_random)
# print(lucky_name)

i = 0
for name in mylist:
    if name == lucky_name:
        print(f"Abe tu pass hoagaya {name}")
        break
    else:
        i+=1
    print(f"Bhak sala tu fail hogaya {name}")