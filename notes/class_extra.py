class Monster:
 # notes to describe function, can print this by calling __doc__
    ''' A monster that has some attribute
    '''
    def __init__(self,health,energy):
        self.health = health
        self.energy = energy

    # private attributes
        self._id = 5 # don't change it for convention

    def attack(self, amount):
        print('The monster has attacked')
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self,speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')

monster = Monster(20,10)

print(hasattr(monster,'health'))
if hasattr(monster,'health'):
    print(f'The monster has {monster.health} health')

setattr(monster,'weapon', 'Sword')
# monster.weapon = 'Sword' same as on top
print(monster.weapon)

new_attributes = (['weapon', 'Axe'], ['armor', 'Sheild'], ['potion', 'mana'])

for attr,value in new_attributes:
    setattr(monster, attr, value)

print(vars(monster))
# setattr(object, 'attribute', value)
# hasattr and setattr
# hasattr(object, 'attribute name')
print(monster.__doc__)
help(monster)