import random

#re write a version of a game and convert it to use OOP

"""
In this simple RPG game, the hero fights the goblin. He has the options to:
1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
"""
class Character:

    def __init__(self, type_char):
        self.type_char = type_char
        if self.type_char == "hero":
            self.name = "Hero"
            self.health = 10
            self.power = 5
        elif self.type_char == "goblin":
            self.name = "Goblin"
            self.health = 6
            self.power = 2
        elif self.type_char == "zombie":
            self.name = "Zombie"
            self.health = 1
            self.power = 1
        elif self.type_char == "medic":
            self.name = "Medic"
            self.health = 10
            self.power = 1
        elif self.type_char == "shadow":
            self.name = "Shadow"
            self.health = 1
            self.power = 2
        elif self.type_char == "wizard":
            self.name = "Wizard"
            self.health = 5
            self.power = 5
        self.print_health_power()
    
    def __str__(self):
        return 'C(%s) : H(%d) : P(%d)' % (self.name, self.health, self.power)

    def attack(self, other_char):
        power = self.power
        # 20 percent chance the hero does double power
        if self.name == "Hero":
            if random.random() <= 0.2: # random.random() returns a value between 0.0 and 1.0
                power = power * 2
                print('\nDouble power mode!')
        if other_char.name == "Shadow":
            if random.random() <= 0.1:
                other_char.health -= power
                print("\n%s does %d damage to the %s." % (self.name, power, other_char.name))
            else:
                print("\n%s attempted to do %d damage to %s, but misses." % (self.name, power, other_char.name))
        else:
            other_char.health -= power
            print("\n%s does %d damage to the %s." % (self.name, power, other_char.name))
        if other_char.name == "Medic":
            if random.random() <= 0.2:
                other_char.health += 2
                print('\nThe medic has healed themselves for 2 points after being attacked.')

        
        if other_char.alive():
            print("The %s's health is now %d" % (other_char.name, other_char.health))
        else:
            # 40% chance that the wizard can ressurect himself
            if other_char.name == "Wizard":
                if random.random() <= 0.4:
                    other_char.health = 5
                    print("The %s was dead, but casted a ressurection spell before the attack was landed." % (other_char.name))
                    print("The %s's health is now %d" % (other_char.name, other_char.health))
            else:
                print("The %s is dead." % (other_char.name))

    def print_health_power(self):
        print("\nThe %s char has %d health and %d power." % (self.name, self.health, self.power))
    
    def alive(self):
        if self.name == "Zombie":
            return True
        else:
            if self.health > 0:
                return True

class Hero(Character):
    def __init__(self):
        Character.__init__(self, "hero")

class Goblin(Character):
    def __init__(self):
        Character.__init__(self, "goblin")

class Zombie(Character):
    def __init__(self):
        Character.__init__(self, "zombie")

class Medic(Character):
    def __init__(self):
        Character.__init__(self, "medic")

class Shadow(Character):
    def __init__(self):
        Character.__init__(self, "shadow")

class Wizard(Character):
    def __init__(self):
        Character.__init__(self, "wizard")

# def char_select():

def main():
    while True:
        mode = input('\nZombie mode(yes, or no)?\n> ').lower()
        harry = Hero()
        # if user wants to play in zombie mode, the dobby is assigned the instance of the zombie class
        if mode == 'yes':
            dobby = Zombie()
            break
        # if user doesn't want to play in zombie mode, then dobby is assigned the instance of the goblin class
        elif mode == 'no':
            dobby = Wizard()
            break
        else:
            print("Invalid input %r" % mode)
    

    while dobby.alive() and harry.alive():
        print("\nWhat do you want the %s to do?\n1. fight %s\n2. do nothing\n3. flee" % (harry.name, dobby.name))
        user_input = input("> ")
        if user_input == "1":
            # Hero attacks goblin
            harry.attack(dobby)
            if not dobby.alive():
                break
        elif user_input == "2":
            # Goblin attacks hero
            dobby.attack(harry)
            if not harry.alive():
                break
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

main()