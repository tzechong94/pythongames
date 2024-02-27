# #means 1 class gets attributes and methods from another class
# # a class can inherit from an unlimited number of other classes
# # a class can also be inherited from by an unlimited of classes

# # can get very complex, most of the time we just need simple inheritance

# class Monster:
#     def __init__(self,health,energy):
#         self.health = health
#         self.energy = energy

#     # methods
#     def attack(self,amount):
#         print('THe monster has attacked!')
#         print(f'{amount} damage was dealt')
#         self.energy -= 20

#     def move(self,speed):
#         print('The monster has moved')
#         print(f'It has a speed of {speed}')

# class Shark(Monster):
#     def __init__(self,speed, health, energy):
#         # Monster.__init__(self,health,energy) # not used anymore
#         super().__init__(health,energy) # use this instead
#         super().move(10)
#         self.speed = speed
#         # need to call parent init method

#     def bite(self):
#         print('The shark has bitten') 

#     def move(self):
#         print('The shark has moved')
#         print(f'The speed of the shark is {self.speed}')
#         #same name overrides parent class

# # exercise

# class Scorpion(Monster):
#     def __init__(self, scorpion_health, scorpion_energy, poison_damage):
#         super().__init__(scorpion_health, scorpion_energy)
#         self.poison_damage = poison_damage
    
#     def attack(self):
#         print('The Scorpion has attacked!')
#         print(f'{self.poison_damage} damage was dealt')

# # create scorpion class that inherits from monster
# # health and energy from parent
# # poision damage attribute
# # overwrite the damage method to show poison damage

# scorpion = Scorpion(scorpion_health=50,scorpion_energy=10,poison_damage=5)
# scorpion.attack()
# print(scorpion.health)
# # shark = Shark(speed = 120, health=100, energy=80)
# # print(shark.health)
# # print(shark.speed)
# # (shark.bite())
# # shark.attack(20)
# # print(shark.energy)
# # shark.move()

# # Method resolution order -> MRO
# # print(Shark.mro())

class Monster:
    def __init__(self, health, energy, **kwargs): #keyword arguments
        self.health = health
        self.energy = energy
        super().__init__(**kwargs) # sets attributes of next class

    def attack(self,amount):
        print('The monster has attacked')
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self,speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')

class Fish:
    def __init__(self,speed,has_scales, **kwargs):
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs) # if there's another class

    def swim(self):
        print(f'The fish is swimming at a speed of {self.speed}')

class Shark(Monster,Fish):
    # mro() shows the order of inheritance
    def __init__(self, bite_strength, health, energy, speed, has_scales):
        self.bite_strength = bite_strength
        super().__init__(health=health, energy=energy, speed=speed, has_scales=has_scales) # goes to next item

shark = Shark(bite_strength=50,health=200, energy=55, speed=120, has_scales=False)
# print(shark.has_scales)
print(shark.speed)