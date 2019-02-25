from leikkipeli import Person

print("Hello Stranger, and welcome to the Awesome Attack Battle 2019! ")
player = Person("García", 500, 100, 50)
enemy = Person("StickyVampire", 500, 100, 50)

García = person.Person
StickyVampire=person.Person

player.stats()
enemy.stats()

running = True
while running:
    print(player.name)
    print("Choose your action: ")
    player.choose_action()
    choice = int(input(">>>: ")) #string not integer in Python3
    action_index = choice - 1
    if action_index == 0:
        damage = player.generate_atk_damage()
        enemy.take_damage(damage)

        print("Ka-boom! You attacked {} and dealt {} damage".format(enemy.name, damage))
    else:
        print(" Choose a correct number")
        continue
    #ENEMY'S TURN
    enemy_choice = 0
    if enemy_choice ==0:
        enemy_damage = generate_atk_damage()
        player.take_damage(enemy_damage)
        print ("Whack! {} attacked {} and dealt {} damage".format(enemy.name, player.name, damage))

player.stats()
enemy.stats()

if player.hp == 0:
    print("You lost!")
    running = False
if enemy.hp == 0:
    print("Great! You won!")
    running = False



#get_stat()
#print(Person)#to print out name, HP/MaxHP, MP/MaxMP
