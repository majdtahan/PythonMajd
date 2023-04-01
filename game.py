#Python game created by Majd El-Tahan to practice Inheritance  

class LivingCreature:
    def __init__(self, name, health, stamina, power_level):
        self.name = name
        self.health = health
        self.stamina = stamina
        self.power_level = power_level

    def attack(self, target):
        pass  # Placeholder method for attacking


class Human(LivingCreature):
    def __init__(self, name, health, stamina, power_level, weapon):
        super().__init__(name, health, stamina, power_level)
        self.weapon = weapon

    def attack(self, target):
        # Calculate damage based on weapon and power level
        damage = self.weapon.damage * self.power_level
        target.health -= damage


class Dragon(LivingCreature):
    def __init__(self, name, health, stamina, power_level, breath_weapon):
        super().__init__(name, health, stamina, power_level)
        self.breath_weapon = breath_weapon

    def attack(self, target):
        # Calculate damage based on breath weapon and power level
        damage = self.breath_weapon.damage * self.power_level
        target.health -= damage



#Game Starting!
answer = input ("Would you like to play the greatest adventure game of all time? (yes/no)")



if(answer.lower().strip() == "yes"):
    name = input("Awesome.. What is your name brave warrior?: ")
    answer = input(name + "... Sounds like a strong warriors name" " ...You've reached a crossroads " + name + ", would you like to go right or left?").lower().strip()
    if answer == "left":
        answer == input("You encountered a dragon, would you like to run or attack? (run/attack)")
        if answer == "attack":
            print("You dealt a total of 0 damage... You died")
        else:
            print("Good choice... you managed to run away safely.")
    
    if answer =="right":
        print("You slipped on a grape... Game Over!")


else:
    print("You're missing out, but see you next time!")