## method and function similar, but method belongs to an object

# test = 'a'

# def test():
#     pass
# a = test
# a.another_attribute = 10
# print(dir(a)) # prints dunder, methods and attributes


# def add(a,b):
#     return a + b

# class Test:
#     def __init__(self, add_function):
#         self.add_function = add_function # passing function

# test = Test(add_function = add)
# print(test.add_function(1,2))

# create a monster class with a parameter called func, store this func as parameter
# create another class called Attacks that has 4 methods: bite, strike, slash, kick (each meothod print some text)
# create a monster object and give it one of the attack methods from the attack class


class Monster:
    def __init__(self, func):
        self.func = func

class Attacks:
    def bite(self):
        print("Monster uses bite")

    def strike(self):
        print("Monster uses strike")

    def slash(self):
        print("Monster uses kick")

    def kick(self):
        print("Monster uses kick")

attacks = Attacks()
monster1 = Monster(func = attacks.bite)
monster1.func()

# every method has a reference to the class, it 
# is easy to get and change class attributes

# methods rely much less on parameters, global and return
# objects can even be influenced from outside and from local 
# scope of a function


# scope problem
# not the cleanest way
def update_health(amount):
    monster.health += amount # can update object even in local scope
# health = 10

# print(health)
# update_health(20)
# print(health)

class Monster: 
    def __init__(self, health, energy):
        self.health = health
        # self.energy = self.set_energy(energy)
        self.set_energy(energy)

    def update_energy(self,amount):
        self.energy += amount

    def set_energy(self, energy):
        new_energy = energy * 2
        self.energy = new_energy

    def get_damage(self,amount):
        self.health -= amount

class Hero:
    def __init__(self, damage, monster):
        self.monster = monster
        self.damage = damage

    def attack(self):
        self.monster.get_damage(self.damage)




monster = Monster(health=100, energy = 50)

hero = Hero(damage=15, monster = monster)
# monster.health += 20
# update_health(20)
# print(monster.health)
# monster.update_energy(20)
print(monster.health)
hero.attack()
print(monster.health)
# exercise 
# create hero class with 2 parameters, damage, monster
# monster class should have a method that lowers the health -> get_damage(amount)
# hero class should have an attack method that calls the get_damage_method from monster
# the amount of damage is hero.damage


        
