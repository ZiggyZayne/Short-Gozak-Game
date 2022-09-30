import random

class player:

    def __init__(self, name, hp, classname, race):
        self.name = name
        self.hp = hp
        self.classname = classname
        self.race = race

    def axeofsea(self, enemy):
        seadmg = random.randint(6, 18)
        enemy.life -= seadmg
        print(f"You deal {seadmg} damage!")

    def cobra(self, enemy):
        cobradmg = random.randint(6, 18)
        enemy.life -= cobradmg
        print(f"You deal {cobradmg} damage!")

    def potion(self):
        potion = random.randint(4, 12)
        print(f"You heal {potion} hitpoints!!")



class enemy:

    def __init__(self, life):
        self.life = life

    def shortsword(self, player):
        ssdmg = random.randint(4, 12)
        player.hp -= ssdmg
        print(f"Enemy attacks with a shortsword, dealing {ssdmg} damage!")

    def bow(self, player):
        bowdmg = random.randint(4, 12)
        player.hp -= bowdmg
        print(f"Enemy attacks with a bow, dealing {bowdmg} damage!")

    def dagger(self, player):
        ddmg = random.randint(2, 10)
        player.hp -= ddmg
        print(f"Enemy attacks with a dagger, dealing {ddmg} damage!")

    def greatsword(self, player):
        gsdmg = random.randint(6, 18)
        player.hp -= gsdmg
        print(f"Enemy attacks with a greatsword, dealing {gsdmg} damage!")

    def poisondag(self, player):
        pddmg = random.randint(12, 24)
        player.hp -= pddmg
        print(f"Enemy attacks with a poisoned dagger, dealing {pddmg} damage!")

gozak = player('Gozak', 75, 'Fighter', 'Goliath')

sebub = enemy(25)


print("You see a bandit with a dagger in his hand approaching quickly. Type bow to fire Cobra!")
x = input()
if x == 'bow':
    gozak.cobra(sebub)
    print(f"Enemy has {sebub.life} hitpoints remaining!")
else: sebub.poisondag(gozak)

print("The enemy slices at you!")
input()
sebub.poisondag(gozak)
print(f"You have {gozak.hp} hitpoints remaining!")
print("The wound burns an unusual amount.")
input()
print("The enemy has drawn in close, type axe to swing the Axe of the Sea!")
y = input()
if y == 'axe':
    gozak.axeofsea(sebub)
    print(f"Enemy has {sebub.life} hitpoints remaining!")
else: gozak.cobra(sebub)
if sebub.life <1:
    print("You are victorious! Press Enter to end the game.")
    input()
    exit()
else: (sebub.poisondag(gozak), print(f"You have {gozak.hp} hitpoints remaining!"),
    input(), print("The enemy still stands! Strike once more by typing axe!"))
z = input()
if z == 'axe':
    gozak.axeofsea(sebub)
    print("You are Victorious! Press Enter to end the game.")
    input()
else: sebub.poisondag(gozak), print(f"You have {gozak.hp} hitpoints remaining"
                                    f"\nWTF are you doing? JUST FOLLOW THE PROMPTS"
                                    "\nWhatever. I'm over it. Game over."), input()





