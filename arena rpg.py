
def vampire():
    #def monster class, with attributes stored in variables
    class Monster:
        def __init__(self, attack, defense, attackrand):
            self.claw = attack
            self.health = defense
            self.attackrange = attackrand
#starting health
    health = 20
#perma while loop combat
    while 1 < 2:
#make vampire
        vampire = Monster('4', '1', random.randint(1,6))
    #attribte 3 defened as attackrange, equal damage now
        damage = (vampire.attackrange - total_armor)
    #health minus damage, equals new ammount
        health -= damage
        print(health)
        if health < 1:
            break
            print(Back.GREEN + vampire.claw)
            print(Fore.RED + vampire.health)
            print(Back.GREEN + vampire.attackrange)


#equipment armor slots, starting values 0
head = 0
chest = 0
feet = 0
hands = 0
arms = 0
legs = 0

#ask if want armor helm, modify equipped armor value
input('Would you like to pick up the hat?')
if 'yes':
    head = 1
    print('You equip the helm +1')
else:
    head = 0
    print('You decide to leave it')

#print post-decision armor value
equiped_armor = [head, chest, feet, hands, arms, legs]
print(equiped_armor)
total_armor = head + chest + feet + hands + arms + legs
print(total_armor)
print('Your total armor is ', total_armor)

import random
battle = input('Will you fight the vampire?')
if 'yes':
    vampire()

'You are at an arena speaking to a registrar. You may sign up for fights with money. Listed in the books are centaur, 2 goblin, brigand, vampire, werewolf, cyclops..'
'Which fight will you register for?'

text adventure.. aasdf... pickup.. pickup.. monster.. monster.. pickup..
xp.. level up..
arena game.. input fight name...

level = 1 + xp/1
xp = 1

if vampire hp <= 0:
    xp += 1

