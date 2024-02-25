class Monster:

# convention to name class with capital letter
    
    # attributes

    def __init__(self, health, energy):
        print("The monster was created")
        # self referring to the health on top, and the health is the parameter for this function
        self.health = health
        self.energy = energy

    def __len__(self):
        return self.health

    def __abs__(self):
        return self.energy
    
    def __call__(self):
        print('THe monster was called')

    def __add__(self,other):
        return self.health + other
    
    def __str__(self):
        return 'A monster'
    #methods
    def attack(self, amount): 
        print("The monster has attacked")
        self.energy -= 20
        print(f'{amount} damage was dealt')
        print(self.energy)

    def move(self, speed): # frist parameter is a reference to the class object itself
        print('The monster has moved')
        print(f'It has a speed of {speed}')


# monster = Monster() # this returns an object
# print(monster.health)
# print(monster.energy)
# monster.attack(40) #TypeError: Monster.attack() takes 0 positional arguments but 1 was given. method needs very least 1 parameter
# # python automatically passes reference object as first parameter
# monster.move(20)



# __dunder__methods (double underscore)
# not called by the user, called by python when something happens
# __init__ is called when the objected is created
# __len__ is called when object is passed into len()
# __abs__ is called when the object is passed into abs()

monster1 = Monster(health = 50, energy = 100)
monster2 = Monster(10,20)
print(len(monster1))
print(abs(monster1))
print(monster1 + 5000)

print(monster1.health)
print(monster2.health)
print(dir(monster1)) #all the dunder methods and attributes
print(monster1.__dict__)

print(str(monster1)) # or monster1, the str dunder prints a string defined rather than the memory reference

