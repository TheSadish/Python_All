class Enemy:
    def __init__(self, atkLow, atkHigh):  # Initialisation Method
        self.atkLow = atkLow  # Set object properties
        self.atkHigh = atkHigh

    def getAttack(self):
        print(self.atkHigh)

enemy1 = Enemy(20,30) # Object 1 
enemy2 = Enemy(30, 45) # Object 2

enemy1.getAttack()

enemy2.atkHigh = 60
enemy2.getAttack()
