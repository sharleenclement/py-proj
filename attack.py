import random

class Enemy:
    
    hp = 200
    
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh
    
    def getAtk(self):
        print("Attack is:", self.atkl)
    
    def getHp(self):
        print("Hp is:", self.hp)

enemy1 = Enemy(90, 100)
enemy1.getAtk()
enemy1.getHp()
enemy2 = Enemy(30, 70)
enemy2.getAtk()
enemy2.getHp()
    
    
playerhp = 300
enemykl = 50
enemykh = 100

while playerhp > 0:
    damage = random.randrange(enemykl, enemykh) # generates random values between start and end point.
    playerhp-=damage
    
    if playerhp <= 50:
        playerhp = 50
    
    print("The damage caused by the enemy is", damage, "and the health of the player is", playerhp)
    
    if playerhp == 50:
        print("You have low health. You've been teleported to the nearest inn.")
        break
