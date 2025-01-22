import random

playerHP = 250
enemyAtklow =  50
enemyAtkHigh = 80

while playerHP > 0:
    damage = random.randint(enemyAtklow, enemyAtkHigh)
    playerHP -= damage

    if playerHP >=30:
        print(f"You are hit, remaining HP is  {playerHP}")
        continue
    print ("Dead")
    break