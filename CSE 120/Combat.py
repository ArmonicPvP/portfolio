import random


attack_sounds = ['Swooooooooosh!!!!!!', 'Clinnnnkk!!!!!', 'Claaannnnnnkkkk!!!!!', 'BOOOOOOOOOOOSSSSHHHHH!!!!!!!!!!', 'dink!', 'CAAAAPPPOOOOWWWWWWW!!!!!']


def attack_dmg():
    return random.randint(1,10)

def roll_d20():
    return random.randint(1, 20)

def potion_heal():
    return random.randint(4, 8)

def combat_round(player_health, player_ac, dmg_mod, enemy_health, enemy_ac, enemy_dmg_roll, used_potion):
    print(f"Player Health: {player_health} | Enemy Health: {enemy_health}")


    while True:

        if not used_potion:
            player_action = input("Choose your action (0: Attack, 1: Potion): ")
        else:
            player_action = input("Choose your action (0: Attack): ")

        if player_action == "0":
            player_attack_roll = roll_d20() + dmg_mod
            print("You rolled {} to hit!".format(player_attack_roll))


            if player_attack_roll >= enemy_ac:
                player_dmg = attack_dmg() + dmg_mod
                enemy_health -= player_dmg
                print(attack_sounds[random.randint(0,5)])
                print("\033[1mYou attack the enemy and deal {} damage.\033[0m".format(player_dmg))

                if enemy_health <= 0:
                    print("\033[1mThe enemy has been defeated!\033[0m")
                    return player_health, enemy_health, used_potion, dmg_mod

            else:
                print("\033[1mYour attack missed!\033[0m")

            if enemy_health > 0:

                enemy_attack_roll = roll_d20()
                print("The enemy rolled {} to hit for its attack!".format(enemy_attack_roll))

                if enemy_attack_roll >= player_ac:
                    enemy_damage = enemy_dmg_roll
                    player_health -= enemy_damage
                    print("Ouchies!!")
                    print("\033[1mThe enemy attacks you and deals {} damage.\033[0m".format(enemy_damage))
                else:
                    print("\033[1mThe enemy's attack missed!\033[0m")


        elif player_action == "1" and not used_potion:
            enemy_dmg = attack_dmg()
            potion_healing = potion_heal()
            print(f"You drink a healing potion and restore {potion_healing} health.")
            print(f"\033[1mThe enemy attacks you and deals {enemy_dmg} damage.\033[0m")
            player_health += potion_healing
            player_health -= enemy_dmg
            used_potion = True



        return player_health, enemy_health, used_potion, dmg_mod


