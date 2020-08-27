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
        self.print_health_power()
    
    def __str__(self):
        return 'C(%s) : H(%d) : P(%d)' % (self.name, self.health, self.power)

    def attack(self, enemy):
        if enemy.name == "Zombie":
            print('\n%s attacks %s and does 0 damage.' % (self.name, enemy.name))
            print("The %s's health is still %d" % (enemy.name, enemy.health))
        else:
            enemy.health -= self.power
            print("\n%s does %d damage to the %s." % (self.name, self.power, enemy.name))
            if enemy.alive():
                print("The %s's health is now %d" % (enemy.name, enemy.health))
            else:
                print("The %s is dead." % (enemy.name))

    def print_health_power(self):
        print("\nThe %s has %d health and %d power." % (self.name, self.health, self.power))
    
    def alive(self):
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
            dobby = Goblin()
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