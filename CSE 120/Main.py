from inventory import Inventory
from Combat import roll_d20
from Combat import attack_dmg
from Combat import potion_heal
from Combat import combat_round
import time
if __name__ =="__main__":
    import random
    import sys
    # variable for if the game has started
    game = 0
    if (game == 0):
        # cultist hp
        cul_hp = random.randint(2, 16)
        # culist armor class
        cul_ac = 12
        # cultist damage
        cul_dmg = random.randint(1, 6) + 1


        # goblin hp
        gob_hp = random.randint(2, 12)
        # goblin armor class
        gob_ac = 15
        # goblin damage
        gob_dmg = random.randint(1, 6) + 2


        # rat swarm hp
        sr_hp = random.randint(7, 56) - 7
        # rat swarm armor class
        sr_ac = 10
        # rat swarm damage calculator
        if (sr_hp >= (sr_hp / 2)):
            sr_dmg = random.randint(2, 12)
        else:
            sr_dmg = random.randint(1, 6)


        #zombie hp
        z_hp = random.randint(3, 24) + 9
        # zombie armor class
        z_ac = 8
        # zombie damage
        z_dmg = random.randint(1, 6) + 1


        # hobgoblin hp
        hgob_hp = random.randint(2, 16) + 2
        # hobgoblin armor class
        hgob_ac = 18
        # hobgoblin damage
        hgob_dmg = random.randint(1, 10) + 1


        # bugbear hp
        bb_hp = random.randint(8, 40) + 5
        # bugbear armor class
        bb_ac = 16
        # bugbear damage
        bb_dmg = random.randint(2, 16) + 2


        # ghoul hp
        gl_hp = random.randint(5, 40)
        # ghoul armor class
        gl_ac = 12
        # ghoul damage
        gl_dmg = random.randint(2, 8) + 2


        # ogre hp
        o_hp = random.randint(7, 70) + 21
        # ogre armor class
        o_ac = 11
        # ogre damage
        o_dmg = random.randint(2, 12) + 4


        # gibbering mouther hp
        gm_hp = random.randint(9, 72) + 27
        # gibbering mouther armor class
        gm_ac = 9
        # gibbering mouther dmg
        gm_dmg = random.randint(5, 30)


        # hellhound hp
        hh_hp = random.randint(7, 56) + 14
        # hellhound armor class
        hh_ac = 15
        # hellhound damage
        hh_dmg = random.randint(1, 8) + 3
        # hellhound fire damage
        hh_fire = random.randint(6, 36)


        # chimera hp
        cm_hp = random.randint(12, 60) + 48
        # chimera armor class
        cm_ac = 14
        # chimera damage
        cm_dmg = random.randint(2, 12) + 4
        # chimera fire damage
        cm_fire = random.randint(7, 56)


        # troll hp
        tr_hp = random.randint(8, 80) + 40
        if (tr_hp >= (tr_hp / 2)):
            tr_hp = tr_hp
        else:
            tr_hp = tr_hp + random.randint(1, 10)
        # troll armor class
        tr_ac = 15
        # troll damage
        tr_dmg = random.randint(2, 12) + 4


        # ettin hp
        et_hp = random.randint(10, 100) + 30
        # ettin armor class
        et_ac = 12
        # ettin damage
        et_dmg = random.randint(2, 16) + 5


        # salamander hp
        sl_hp = random.randint(12, 120) + 24
        # salamander armor class
        sl_ac = 15
        # salamander damage
        sl_dmg = random.randint(2, 12) + 4
        # salamander fire damage
        sl_fire = random.randint(1, 6)


        # young black dragon hp
        drg_hp = random.randint(15, 150) + 45
        # young black dragon armor class
        drg_ac = 18
        # young black dragon damage
        drg_dmg = random.randint(2, 20) + 4
        # young black dragon acid damage
        drg_acid = random.randint(8, 88)



        # cultist stats
        cultist = [cul_hp, cul_ac, cul_dmg]
        # goblin stats
        goblin = [gob_hp, gob_ac, gob_dmg]
        # swarm of rats stats
        swarm_of_rats = [sr_hp, sr_ac, sr_dmg]
        # zombie stats
        zombie = [z_hp, z_ac, z_dmg]
        # hobgoblin stats
        hobgoblin = [hgob_hp, hgob_ac, hgob_dmg]
        # bugbear stats
        bugbear = [bb_hp, bb_ac, bb_dmg]
        # ghoul stats
        ghoul = [gl_hp, gl_ac, gl_dmg]
        # ogre stats
        ogre = [o_hp, o_ac, o_dmg]
        # gibbering mouther stats
        gibbering_mouther = [gm_hp, gm_ac, gm_dmg]
        # hellhound stats
        hellhound = [hh_hp, hh_ac, hh_dmg, hh_fire]
        # chimera stats
        chimera = [cm_hp, cm_ac, cm_dmg, cm_fire]
        # troll stats
        troll = [tr_hp, tr_ac, tr_dmg]
        # ettin stats
        ettin = [et_hp, et_ac, et_dmg]
        # salamander stats
        salamander = [sl_hp, sl_ac, sl_dmg, sl_fire]
        # young black dragon stats
        young_black_dragon = [drg_hp, drg_ac, drg_dmg, drg_acid]


        # creates the 2d arrays for monster names and monsters
        names = [['Cultist', 'Goblin', 'Zombie'], ['Hobgoblin', 'Swarm of Rats', 'Ghoul'],
                 ['Bugbear', 'Ogre', 'Gibbering Mouther'], ['Hellhound', 'Troll', 'Ettin'],
                 ['Salamander', 'Chimera', 'Young Black Dragon']]
        monsters = [[cultist, goblin, zombie], [hobgoblin, swarm_of_rats, ghoul],
                    [bugbear, ogre, gibbering_mouther], [hellhound, troll, ettin],
                    [salamander, chimera, young_black_dragon]]



        group = random.randint(0, 4)
        encounter = random.randint(0, 2)
    # ask player if they are ready to start
    begin = input('"Hello Adventurer! Are you ready to begin your journey of a lifetime?" (Type Yes or No): ')          #recent change!!!!!!!!! inputs with .lower() got rid of extra "
    # check if they typed yes or no
    if (begin.lower() == "yes" or "no"):
        # start
        if (begin.lower() == "yes"):
            print('"Wonderful! I will be your Game Master for this game. Let''s get started!"')
        # don't start
        elif (begin.lower() == "no"):
            print('"Well I''m sorry to hear that. Please come again when you''re ready."')
        # they didn't type yes or no
        else:
            begin = input('"I''m sorry, I don''t quite understand your answer. Can you try again?" (Type Yes or No): ')
    # ask them if they are ready again
    while (begin.lower() == "no"):
        begin = input('"Are you ready to begin now?" (Type Yes or No): ')


    # create our character sheet array
    character_sheet=[]
    while (begin.lower() == "yes"):
        # get character name
        character_name = input('"What shall I call you? Adventurer just doesnt have that nice ring to it." (Please enter a name): ')
        # append to character sheet
        character_sheet.append(character_name)
        print('"Nice to meet you',character_name,'"')
        break
    while (begin.lower() == "yes"):
        # get character race
        character_race = input('"My eyes are starting to cloud with age so might I ask, what are you?" (Please type Human, Dwarf, or Elf): ')
        # if they picked Dwarf
        if character_race.lower() == "dwarf":
            print('"Ah! A',character_race,'eh? The town of Phandalin hasnt seen one of the Deep Folk for quite some time."')
        # if they picked Human
        elif character_race.lower() == "human":
            print('"Ah yes, welcome to the town of Phandalin,',character_name,', I''m sure you will fit right in!"')
        # if they picked Elf
        elif character_race.lower() == "elf":
            print('"Really, an honest to good',character_race,'? The faire folk havent left their forests for ages. Welcome to the town of Phandalin!"')
        # if they didn't type a valid class
        else:
            character_race = input('"I''m sorry, I must have misheard you. Can you please repeat that?" (Please type Human, Dwarf, or Elf): ')          #recent change!!!!!! got rid of "continue" and set else statement to define character_race so beginning print statement wouldn't copy again.
            continue
        # append to character sheet
        character_sheet.append(character_race)
        # character class is always Fighter
        character_class = "Fighter"
        # append to character sheet
        character_sheet.append((character_class))
        break
    # randomly select a strength
    strength = random.randint(14, 18)
    # randomly select an armor class
    armor_class = random.randint(13, 16)
    # set hp
    hit_point_maximum = 20
    # sword
    sword_up = 0
    # experience
    experience_points = 0
    # level
    character_level = 1
    # randomly give an amount of gold in 25 increments
    gold = random.randrange(200, 300, 25)
    # amount of health potions
    health_potions = 1


    # Elf gets bonus AC
    if (character_race.lower() == "Elf"):
        armor_class += 1
    # Human gets bonus Strength
    if (character_race.lower() == "Human"):
        strength += 1
    # Dwarf gets bonus HP
    if (character_race.lower() == "Dwarf"):
        hit_point_maximum += 2
    # set their current HP to their maximum HP
    current_hp = hit_point_maximum
    # check to make sure they don't have extra HP
    if current_hp >= hit_point_maximum:
        current_hp = hit_point_maximum
    else:
        current_hp = current_hp
    # assign stats names to a dict
    stats = dict([
        ('Strength', strength),
        ('AC', armor_class),
        ('HP', hit_point_maximum),
        ('EXP', experience_points),
        ('Level', character_level),
        ('Gold', gold)
    ])
    print('"It has been an honor to meet you friend! Allow me to cast a quick spell to see what youre made of!\n"*magical whooshing noises*"')       #recent change!!!!!!!!!!!!!!!!!
    print('"Wow! Take a look at you!"')                                                                                                              #recent change!!!!!!!
    print(character_sheet)
    print(stats)
    input('(Press Enter to begin your tale)')


    # rumors known
    rumors = 0
    # how many inn visits
    inn_visits = 0
    # how many armory visits
    armory_visits = 0
    # how many orchard visits
    orchard_visits = 0
    # how many shrine visits
    shrine_visits = 0
    # how many cave visits
    cave_visits = 0
    # how many times slept
    nights_slept = 0
    # has Daran been helped
    daran_helped= 'no'
    # has the shrine been cleared
    shrine_cleared= 'no'
    # what turn are we on
    turn_count = 1


    # actions array
    action = [0, 1, 2]
    # HP restoration calculator
    hp_restore = random.randint(2, 8) + 2


    # options in combat array
    combat_option =['0) Swing your sword', '1) Drink a health potion', '2) Attempt to flee']
    # town locations array
    town_locations=['0) The Stonehill Inn','1) Lionshield Coster','2) Edermath Orchard']
    # inn options array
    inn_options = ['0) Ask for a room to stay (-15g)','1) Ask about buying supplies','2) Ask about any rumors', '3) Leave']
    # armory options array
    armory_option = ['0) Upgrade Sword -100g pieces','1) Upgrade Shield -150g pieces','2) Buy Health Potion -50g piecs', '3) Leave']
    # orchard options array
    orchard_options=['0) Ask about work','1) Ask about monsters','2) Ask about training', '3) Leave']
    # outside cave choices array
    lost_cave_options = ['0) Walk into the cave','1) Run away from the cave']
    # inside cave choices array
    cave_split = ['0) Take the left path','1) Take the right path']

    print('The dirty track that the locals call a road emerges from a wooded hillside, and you catch your first glimpse of Phandalin.\n','The town consists of forty or fifty simple log buildings, some build on old fieldstone foundations.')
    print('More old ruins, crumbling stone walls covered in ivy and briars, surround the newer houses and shops, showing how this must have been a much larger town in centuries past.\n','As you approach, you see children playing on the town green and townsfolk tending to chores or running errand at shops.')
    print('Many people look up as you approach, but all return to their business as you walk on by.')



    while True:


        for town in town_locations:
            print(town)
        # store where they go
        direction = input("Where would you like to go? (Please type the corresponding number and press Enter):")
        # if they type 0
        if (direction == '0'):
            # if they've never visited the inn before
            if (inn_visits == 0):
                print('In the center of town stand a large, newly built roadhouse of fieldstone and rough-hewn timbers.\n', 'The common room is filled with locals nursing mugs of ale or cider, all of them eyeing you with curiosity.')
                print('A short, friendly young human male named Toblen Stonehill introduces himself as the owner and waves you over to his bar.')
                print('"Greetings there stranger! Always fun to see a new face around here. What can I do for you today?"')
                input('(Press Enter to see menu options)')
            # if they have
            else:
                print('As you wonder into the inn, Toblen looks up from polishing a class and calls out to you.')
                print('"Welcome back',character_name,'. What can I do for you?"')
                input('(Press Enter to see menu options)')
            while True:
                for option in inn_options:
                    print(option)
                # store the inn choice they make
                inn_choice = input('(Please make a selection): ')
                # if they choose 0 and have enough gold
                if (inn_choice == '0' and gold >= 15):
                    # take 15 gold
                    gold -= 15
                    # update gold count
                    stats['Gold'] = gold
                    # heal to full
                    current_hp = hit_point_maximum
                    # add a slept night
                    nights_slept += 1
                    print('"Sure thing! We have an open room upstairs that can be yours for the night. Just let me know if you need anything else"')
                    input('As you rest your tired body for the night, you feel your vitality start to be restored. (Press Enter to sleep)')
                    print('Your HP has been reset! Current HP =',hit_point_maximum)
                # if they choose 0 and don't have enough gold
                elif (inn_choice == '0' and gold < 15):
                    print('"I''m sorry, but you dont appear to be able to afford a room right now. Come back later when you have at least 15gp and we can work it out"')
                # if they choose 1
                elif (inn_choice == '1'):
                    print('"Looking to upgrade your gear or keeping yourself alive out there? Head over to the Lionshield Coster and Linene will take goood care of you.\n','I know she seems harsh, but trust me, she has a good heart and does honest work."')
                # if they choose 2 and know a rumor
                elif (inn_choice == '2' and rumors == 1):
                    print('"Rumor has it that the Cragmaw Goblins have moved into Lost Echo Cave just outside of town. I dont know what would casue them to mobilize so suddenly, but it has a lot of the townsfolk scared out of their mind.\n','I know it would go a long way in their eyes if a brave adventurer such as yourself were to help clear them out."')
                    input('(Lost Echo Cave has been added to your map)')
                    # add to rumors
                    rumors+= 1
                    # add a new town location
                    town_locations.append('4) Lost Echo Cave')
                # if they choose 2 and know no rumors
                elif (inn_choice == '2' and rumors == 0):
                    print('"I''ve heard that some shady folks have been lurking around the Shrine of Luck lately. Some are calling them dragon worshippers, but I just call them spooky.\n','You can find the shrine just south of town."')
                    input('(Shrine of Good Luck has been added to your map)')
                    # add to rumors
                    rumors += 1
                    # add a new town location
                    town_locations.append('3) Shrine of Good Luck')
                # if they choose 2 and know at least 2 rumors
                elif (inn_choice == '2' and rumors>=2):
                    print('"Sorry',character_name,', but nothing has reached my ears since we last spoke"')
                # if they choose 3 and have no inn visits
                elif (inn_choice == '3' and inn_visits == 0):
                    print('"It was nice to meet you',character_name,'. Please come again whenever you need a place to rest or just wanna chat."')
                    inn_visits += 1
                    break
                # if they choose 3 and have at least 1 inn visit
                elif (inn_choice == '3' and inn_visits >= 1):
                    print('"Have a good day',character_name,'! Hope to see you around soon."')
                    inn_visits += 1
                    break
                # if they don't put in valid a number
                else:
                    print('"Sorry I must have cotton in my ears. Could you repeat that?"')
        # if they type 1
        elif (direction == '1'):
            # if they've never been to the armory
            if (armory_visits == 0):
                print('Hanging above the front door of this modest trading post is a sign shaped like a wooden shield with a blue lion painted on it.')
                print('A sharp tongued human woman who seems to be in her mid-thirties addresses you as you walk in.\n''"I''ve heard there was a new',character_race,'in town today. Name''s Linene, pleasure to meet you."')
                print('"What can me and my crew do for you today?"')
                input('(Press Enter to see menu options)')
            # if they have been to the armory
            else:
                print('You feel the heat of the forge hit your face as you walk in the door.\n', 'You hear Linene barking orders to a couple of her crew members.\n''She turns to look at you as the bell above the door rings and you step in.')
                print('"Oh hey there',character_name,'! Sorry about the noise. What can I do for you today?"')
                input('(Press Enter to see menu options)')
            while True:
                for option in armory_option:
                    print(option)
                print('(You have',gold,'gp left)')
                # store the armory choice they make
                armory_choice = input('(Please make a selection): ')
                stats['Gold'] = gold
                # if they select 0
                if (armory_choice == '0'):
                    # if they don't have enough gold
                    if (gold < 100):
                        print('"I''m sorry, you don''t seem to have enough gp to purchase this."')
                    # if they do
                    else:
                        # take away 100 gold
                        gold -= 100
                        # level up their sword
                        sword_up += 1
                        print('Your damage has increased by 1!', 'You have', gold, 'left.')
                # if they select 1
                elif (armory_choice == '1'):
                    # if they don't have 150 gold
                    if (gold < 150):
                        print('"I''m sorry, you don''t seem to have enough gp to purchase this."')
                    # if they do
                    else:
                        # take away 150 gold
                        gold -= 150
                        # add 1 to AC
                        armor_class += 1
                        print('Your AC has increased by 1!', 'You have', gold, 'left.')
                # if they select 2
                elif (armory_choice == '2'):
                    # if they don't have 50 gold
                    if (gold < 50):
                        print('"I''m sorry, you don''t seem to have enough gp to purchase this."')
                    else:
                        # take away 50 gold
                        gold -= 50
                        # give 1 health potion
                        health_potions += 1
                        print('Drink me to regain 2d4 HP!', 'You have', gold, 'left.')
                # if they select 3
                elif (armory_choice == '3'):
                    print('"Pleasure doing business with you, please come again."')
                    # add an armory visit
                    armory_visits += 1
                    break
                # if they don't type a valid number
                else:
                    print('"Sorry, my hearing ain''t so good from all the loud hammer work. Can you repeat that?"')
        # if they select 2
        elif (direction == '2'):
            # if this is their first visit
            if (orchard_visits == 0):
                print('When you first entered the town of Phandalin from atop the hill, you noticed a quaint apple orchard in full bloom despite the rugged landscape and its ruins.\n','You decide to pay the small patch of greenery a visit. As you walk through the front gate, you notice a half-elf gentleman, silver-haired from a life longer than any human.\n','He introduces himself as Daran Edermath, a retired adventurer turned farmer.')
                input('(Press Enter to continue)')
                print('"Welcome to Phandalin friend. Hope everyone has been treating you kindly. Anything I can help you with, one outsider to another?"')
            # if you've been there before
            else:
                print('You walk the familiar path into Darans orchard. The trees slightly emptier of their fruits than last time you visited.\n','The breeze rustles the leaves as a voice calls to you from behind.')
                input('(Press Enter to continue)')
                print('"Hail',character_name,'! Is there something you need of this old man?"')
            while True:
                for option in orchard_options:
                    print(option)
                orchard_choice = input('(Please make a selection): ')
                # if they select 0
                if (orchard_choice == '0'):
                    print('Daran lets out a small chuckle before answering.\n','"Sorry friend and no offense, but you don''t seem like the farmer type. But, if you are truly interested, I can always use some help picking apples.\n','I would hate for them to go bad on the vine. Help me out for a day and I''m willing to pay a small fee."')
                    # are they working?
                    working = input('(Help Daran for the day? Yes or No)')
                    # if no - .lower() ensures that the string is all lowercase
                    if (working.lower() == 'no'):
                        print('"Well that''s okay. No hard feelings, eh?"')
                    # if yes
                    elif (working.lower() =='yes'):
                        print('"Well that''s mighty kind of you. Let me show you to where you will be working today.\n','When you''re done, just come find me, and I will make sure you get paid and have a place to rest."')
                        input('(Press Enter to start your work)')
                        # add 25 gold
                        gold += 25
                        # add a night slept
                        nights_slept += 25
                        # heal to full
                        current_hp = hit_point_maximum
                        print('After a day of honest work, you go to sleep in the loft of the barn.\n','Daran has paid you 25gp.')
                        print('Total gold:',gold)
                        input('(Press Enter to return to the menu)')
                    # if they don't type yes or no
                    else:
                        print('(Input was invalid. Please type "yes" or "no")')
                # if they select 1
                elif (orchard_choice == '1'):
                    print('"So you wanna know about monsters huh? Well I guess you''re asking the right guy.\n','Monsters like to gather in groups depending on their strength. The further into a dungeon you go, the stronger and more dangerous the monsters become.\n','The stronger the monsters, however, the better the rewards they drop and the stronger you become. Never be too afraid to run when the fight gets too rough though."')
                    input('(Press Enter to continue)')
                    print('"All monsters and adventures have an armor class, AC for short. This determines how hard it is for them to hit you and vise versa.\n','Usually, the larger or slower the monster is, the lower their AC becomes. However, that generally means their hit points are a little bulkier.\n','The same logic works in reverse. The small, quick fellows are harder to hit but take less effort to dispatch.')
                    input('(Press Enter to continue)')
                    print('Then, there''s the big bad monsters that you should hope to never encounter alone. Beasts like the Chimera or Dragons.\n','These guys are the baddest of the bad and have been the end of many adventurers."')
                    print('Daran gives an audible sigh as a hint of sadness crosses his face.')
                    print('"Well then, sorry about that. Was there something else I can do for you',character_name,'?"')
                    input('(Press Enter to see options)')
                # if they select 2
                elif (orchard_choice == '2'):
                    # have you helped daran yet?
                    if (daran_helped== 'no'):
                        print('"Training huh? There might be a few things I can teach you. Unfortunately, time hasn''t been as kind to me as you have.\n','If I had a couple health potions I would be able to keep up better. You wouldn''t happen to have any, would ya?"')
                        input('(Press Enter to continue)')
                        print('Health Potions:',health_potions)
                        # store if they help Daran
                        training = input('(Give Daran 2 health potions? Yes or No)')
                        # if they say yes and have enough potions
                        if (training.lower() == "yes" and health_potions >= 2):
                            # take 2 potions
                            health_potions -= 2
                            # increase amount
                            increase = random.randint(5, 10)
                            # add to max HP
                            hit_point_maximum += increase
                            # add to current HP
                            current_hp += increase
                            # set daran_helped to yes
                            daran_helped= 'yes'
                            # save new stats
                            stats["HP"] = hit_point_maximum
                            print('Health Potion:', health_potions)
                            print('"Well would you look at that!"n\'','Daran takes the potions and drinks them. A look of relief crosses his face as he stands a little straighter.\n','"Right then! Lets get to it.')
                            input('(Press Enter to continue)')
                            print('After a rigorous sparring session, you feel more confident in your abilities.\n',
                                  'Your Hit Point Maximum has increased to:',hit_point_maximum)
                            print(stats)
                        # if you say no or don't have enough potions
                        elif (training.lower() == 'no' or health_potions < 2):
                            print('Health Potion: ',health_potions)
                            print('"Ah, that''s too bad. Maybe some other time then...')
                            input('(Press Enter to return to the menu)')
                    # if you have helped Daran
                    else:
                        print('"Sorry',character_name,'it looks like you already know all I can teach you')
                        input('(Press Enter to return to the menu)')
                # if they select 3 and haven't been to the orchard
                elif (orchard_choice == '3' and orchard_visits == 0):
                    print('"Well it was an honor to meet a fellow adventurer. I wish you the best of luck and hope to see you around."')
                    # add a visit
                    orchard_visits += 1
                    break
                # if they select 3 and have been to the orchard
                elif (orchard_choice == '3' and orchard_visits >= 1):
                    orchard_visits=orchard_visits+1
                    print('"Well, thanks and coming to visit once more. Glad to see you''re still up kicking."')
                    orchard_visits += 1
                    break
                # if they select 4
                elif (orchard_choice == '4'):
                    print('You pull out the crumbled letter found on the corpse of your attempted murderer and show it to Daran.\n','He squints his eyes as he attempts to read the scrawlings \n','As he reads through the note you notice him getting paler \n','"This is a note detailing how to open a portal to another realm, the cult must be trying to summon Voldemort"')
                    print('"Sorry I wasn''t much help',character_name,'. Is there something else I can help you with though?"')
                # if they don't type a vlid number
                else:
                    print('"I know I''m old, but I didn''t think my hearing at left just yet. What did you say?"')


        elif (direction == '3'):
            while True:
                if (shrine_cleared=='no' and cul_hp>0):
                    print('The only place in Phandalin resembling a temple is a small shrine made of stones taken from the nearby ruins.\n',
                          'You see carved into the rock, a symbol of what appears to be a coin tossed into a wishing well.')
                    print('You recognize this to be the symbol of Tymore, goddess of luck and good fortune. However, something seems off about the carving.')
                    decision=input('(Do you wish to investigate further? yes or no?)')
                    if (decision=='yes'):
                        print('You take a closer look at the symbol and notice theres a few marks scratched into the stone.\n',
                              'They appear to depict a crude drawing of some sort of lizard head on the coin.\n',
                              'Absorbed in thought as to what this must mean, you fail to hear the soft footsteps creeping up behind you.')
                        input('(Press Enter to continue)')
                        print('A hand firmly grasps and spins you around as you feel a knife stick into your side.\n',
                              'You take',cul_dmg,'damage as you look into the mask covered face of a grinning stranger')
                        current_hp = current_hp-cul_dmg
                        print('(You have',current_hp,'HP remaining!)')
                        input('(Press Enter to begin combat.Good Luck!)')
                        while True:
                            cul_hp = cul_hp
                            turn_count = turn_count
                            print(character_name,"'s HP remaining:",current_hp,'\n','Cultist HP remaining:',cul_hp)
                            if (turn_count % 2 and current_hp>0):
                                print("It is your turn! What would you like to do?")
                                for i in combat_option:
                                    print(i)
                                action = int(input('(Choose your combat action)'))
                                if action == 0:
                                    input('(Press Enter to roll to hit)')
                                    player_to_hit=int(random.randint(1,20)+((strength-10)/2))
                                    print('You rolled a',player_to_hit)
                                    if player_to_hit>=cul_ac:
                                        player_damage = int(random.randint(1, 10) + (strength - 10) / 2)+sword_up
                                        print('You swing your sword and catch your enemy unprotected.\n'
                                        'You deal', player_damage, 'damage to the enemy.')
                                        cul_hp=cul_hp-player_damage
                                        turn_count=turn_count+1
                                    else:
                                        print('You swing your sword but your enemy dodges out of the way, avoiding the blow')
                                        turn_count=turn_count+1
                                elif action==1:
                                    if health_potions>0:
                                        print('You reach into your pocket and pull out a health potion and down it in one breath')
                                        current_hp=current_hp+hp_restore
                                        turn_count=turn_count+1
                                    else:
                                        print('You reach into your pocket to look for a potion and find an empty bottle.\n',
                                                'You swear under your breath as you rethink your next action')
                                elif action==2:
                                    flee=random.randint(1,20)
                                    if flee>=10:
                                        print('You roll out of the way as the monster swipes at you. Time to get back to safety!')
                                        turn_count=1
                                        break
                                    else:
                                        print('You try to roll out of the way but your shield gets caught underneath you.\n',
                                                'You look back to see the enemy hot on your heels!')
                                        turn_count=turn_count+1
                            else:
                                monster_to_hit=random.randint(1,20)+3
                                print('The Cultists rolls to hit')
                                print('They rolled a',monster_to_hit)
                                if monster_to_hit>=armor_class:
                                    print('The cultists thrust in his knife under your shield and in between your armor!')
                                    print('You take',cul_dmg,'damge.')
                                    current_hp=current_hp-cul_dmg
                                    turn_count=turn_count+1
                                    if current_hp>0:
                                        input('(Press Enter to take your turn)')
                                    else:
                                        print('As the knife sinks into your chest, your eyes grow heavy and you vision starts to dim\n',
                                              'This is the end of you adventure')
                                        input('(Press Enter to Finish the game')
                                        sys.exit('Im sorry it ended. Please come back and try again')
                                else:
                                    print('The cultists swings wildly with his knife but you raise your shield just in time to block')
                                    input('(Press Enter to take your turn)')
                                    turn_count=turn_count+1
                            if cul_hp <= 0:
                                print('As the cultists charges forward, you see an opening in his stance.\n',
                                  'You thrust out your sword, impaling the mad man and running him through.\n',
                                  'You take a moment to catch your breath as his limp body drops to the ground.')
                                print('(You gain 100 EXP!)')
                                experience_points = experience_points + 100
                                stats["EXP"]=experience_points
                                turn_count = 1
                                print(stats)
                                input('(Press Enter to Continue)')
                                break
                    elif decision =='no':
                        print('Come back later when this is done and tested')
                        break
                    else:
                        print('(Please Enter a valid input')
                else:
                    if shrine_cleared == 'no':
                        print('With the cultist dispatched, you look around and see a bloody letter in the grass.\n'
                            'Its in an language unknown to you, consisting mostly of scribbles and crude drawings.\n',
                            'Maybe someone in town may know something?')
                        shrine_cleared = "yes"
                        orchard_options.append('4) Ask about Cultist note')
                        print('(New Orchard option unlocked)')                   #recent change!!!!!!!!!!
                        print('New rumor available in the inn')
                        input('(Press Enter to continue)')
                        break
                    break
        elif (direction == '4'):

            restart_cave = True
            while restart_cave:

                current_hp = hit_point_maximum

                bp = Inventory("Backpack", contents=None)
                bp.add("Torch", 0)
                bp.add("Moldy piece of bread", 0)
                bp.add("Strange looking crest with ancient symbols", 0)
                dmg_mod = 2
                player_succeeded = True
                while player_succeeded:
                    current_hp = hit_point_maximum

                    player_succeeded = False

                    print("As you crest a hill, a hole in the earth appears before you, there are a few corpses piled up at the entrance to the cave")
                    print("\"This must be the Lost Echo Cave the innkeeper was talking about\" You think to yourself")
                    print("Do you wish to:")
                    for option in lost_cave_options:
                        print(option)
                    lost_cave_input = input("Please choose an option: ")

                    if lost_cave_input == '1':
                        break

                    elif lost_cave_input == '0':
                        print("As you walk into the cave, the ground begins to shake. Suddenly you feel something land on top of you knocking you to the ground.")
                        print("Your eyes slowly adjust to the darkness you see that the entrance you just walked through is now blocked by boulders. You push whatever fell on you off and notice it is a skeleton wearing a relatively unharmed bag.")
                        print("You open the bag, hoping to find something to aid you in your journey")
                        print(bp)
                        input("(Press Enter to Proceed)")
                        print("Satisfied with the bag's content's you peer deeper into the cave")
                        print("You see the cave breaking into two pathways.\n Looking down the left pathway, you can see a dull light shining from far away.\n Examining the right pathway, you swear you can hear a high pitched voice rambling to itself")


                        for option in cave_split:
                            print(option)
                        cave_split_option = input("Which path will you take? ")

                        if cave_split_option == '0':
                            print("Moving down the left pathway, a dull light shines further down the path. Curiously, you hear a distant rumbling from behind you")
                            print("Approaching the light source, it's revealed that a camp of goblins is occupying this part of the cave")
                            print("You creep into the camp, looking to sneak through. You start to feel raindrops on your head, \'Isn\'t this a cave?\' You think")
                            print("Looking up find the clouds, you are instead greeted with a deafening snarl and the worst smell you can ever remember encountering. A goblin stares back at you angrily as you leap away")
                            print("Roll for Initiative!")
                            #Goblin Fight here

                            while current_hp > 0 and gob_hp > 0:
                                current_hp, gob_hp, used_potion, dmg_mod = combat_round(current_hp, armor_class, dmg_mod, gob_hp, gob_ac, gob_dmg, used_potion=False)

                            print("Passing through the goblin\'s territory you find a sword that shines brightly despite the low amount of light")
                            bp.add("Dawnbreaker",0)
                            print("(Dawnbreaker was added to the traveler\'s bag)")
                            dmg_mod += 2

                        if cave_split_option == '1':
                            print("The right pathway was more inviting, so you begin your trek that way instead")
                            print("Soon a troll appears before you, blocking travel further into the cave. As he stops rambling to examine you, you can almost make out a rumbling sound from the direction you entered")
                            print("The troll speaks to you \"You have to answer Bogart\'s riddles of three if you wish to pass Bogart\'s lair\"")
                            print("\"I am always in front of you but can’t be seen\"")
                            riddle_answer1 = input("What am I?\n0) Your Nose\n1) The Future\n2) The IRS\n3) Give Up\n")
                            answered_riddle1 = False
                            while not answered_riddle1:
                                if riddle_answer1 == '3':
                                    print("I knew my riddles were impossible to solve! Now Bogart will show you what happened to the last travellers who came through here!")
                                    print("You tasted Bogart\'s wrath")
                                    input("(Press enter to continue)")
                                    current_hp = 0
                                    break

                                if riddle_answer1 == '1':
                                    print("Good, now for the second riddle!")
                                    answered_riddle1 = True
                                else:
                                    print("\"NOPE!!\" he cackles, \"Will You try again or give up?!\"")
                                    riddle_answer1 = input("What am I?\n0) Your Nose\n1) The Future\n2) The IRS\n3) Give Up\n")
                            if current_hp > 0 and answered_riddle1:
                                print("What goes up but never comes down?")
                                riddle_answer2 = input("0) A Rocketship\n1) Gas Prices\n2) Your age\n3) Give Up\n")
                                answered_riddle2 = False
                                while not answered_riddle2:
                                    if riddle_answer2 == '3':
                                        print("I knew my riddles were impossible to solve! Now Bogart will show you what happened to the last travellers who came through here!")
                                        print("You tasted Bogart\'s wrath")
                                        input("(Press enter to continue")
                                        current_hp = 0
                                        break

                                    if riddle_answer2 == '2':
                                        print("Nobody's ever answered two of my riddles! But be warned the last will be the hardest!")
                                        answered_riddle2 = True

                                    else:
                                        print("WRONG!! I\'d bet the Give Up button looks really tempting right now!")
                                        riddle_answer2 = input("0) A Rocketship\n1) Gas Prices\n2) Your age\n3) Give Up\n")

                            if current_hp > 0 and answered_riddle2:
                                print("The more of this there is, the less you see. What is it?")
                                riddle_answer3 = input("0) Darkness\n1) Light\n2) Beer\n3) Give Up\n")
                                answered_riddle3 = False

                                while not answered_riddle3:
                                    if riddle_answer3 == '3':
                                        print("I knew my riddles were impossible to solve! Now Bogart will show you what happened to the last travellers who came through here!")
                                        print("You tasted Bogart\'s wrath")
                                        input("(Press enter to continue)")
                                        current_hp = 0
                                        break

                                    if riddle_answer3 == '0':
                                        print("NOOOOOO! No one has ever answered all of Bogart\'s riddles before! It seems Bogart must let you pass")
                                        answered_riddle3 = True
                                        print("Moving past Bogart, who has begun to ramble once again, you pass pile of shiny objects most likely belonging to those who failed the riddles. Gleaming at the top of the pile is a sturdy looking shield")
                                        print('(Duskguard added to inventory)')
                                        bp.add("Duskguard", 0)
                                        armor_class += 2
                                    else:
                                        print("I knew this one would get you! Don\'t be bothered to try again!")
                                        riddle_answer3 = input("0) Darkness\n1) Light\n2) Beer\n3) Give Up\n")



                    if current_hp > 0:
                        player_succeeded = True
                        break
                    else:
                        print("I hope it works this time")
                        input()
                if lost_cave_input != '0':
                    restart_boss_fight = False
                    break
                if current_hp <= 0:
                    restart_input = input("Your HP hit 0, you were defeated.\nWould you like to restart from the beginning of the cave? (yes/no): ").lower()
                    if restart_input == "yes":
                        # The outer while loop for restart_cave will continue, and the player will reset from the beginning of the cave
                        continue
                    else:
                        restart_game = False
                        print("Thank you for playing the Adventure Game!")



                elif player_succeeded:
                    print("Continuing your journey deeper into the cave, you enter a cavern and end up face to face with a massive cell door")
                    open_bag = input("You seem to notice something glowing in your traveler\'s bag. Would you like to open it? (yes/no) ").lower()
                    if open_bag == 'yes':
                        print("The strange crest is glowing as if reacting to the seal on the door, the moldy bread also looks pretty enticing right about now")
                        bag_choice = input("What would you like to do?\n0) Eat the moldy bread\n1) Touch the glowing crest to the seal\n")
                        if bag_choice == '0':
                            print("You grab the moldy bread out of the bag and eat it. It\'s not as bad as you expected it to be, but you don't any less hungry")
                            print("The wall in front of you seems to be reacting differently, however, it seems like it\'s charging at you")
                            print("CRACK!!")
                            print("\'Maybe the bread wasn't worth it\' You think as you slump against the wall, the light in your eyes being replaced by a crimson red from the gash on your head")
                            print("Better luck next time")
                            input("(Press enter to continue)")
                            current_hp = 0
                            if current_hp > 0:
                                player_succeeded = True
                                break
                        if current_hp <= 0:
                            restart_input = input(
                                "Your HP hit 0, you were defeated.\nWould you like to restart from the beginning of the cave? (yes/no): ").lower()
                            if restart_input == "yes":
                                # The outer while loop for restart_cave will continue, and the player will reset from the beginning of the cave
                                continue
                            else:
                                restart_game = False
                                print("Thank you for playing the Adventure Game!")
                        elif bag_choice == '1':
                            print("The crest seems to pull your hand to the seal on the door. As they make contact an oppressive light suddenly dominates your surroundings.")
                            print("Once the light has faded, you push forwards into the now opened cell. \'There\'s no turning back now\' You think")
                            break

                    else:
                        print("The rumbling sound you heard earlier is back, and sounds a lot angrier now.")
                        print("A massive boulder can barely be made out rumbling towards you very quickly. You turn to try and run away, but the cell door stands steadfast determined to face it\' new attacker with you as it\'s unwilling ally.")
                        print("You are stuck between a rock and a hard place")
                        input("(Press enter to continue)")
                        current_hp = 0
                        if current_hp > 0:
                            player_succeeded = True
                            break

                    if current_hp <= 0:
                        restart_input = input(
                            "Your HP hit 0, you were defeated.\nWould you like to restart from the beginning of the cave? (yes/no): ").lower()
                        if restart_input == "yes":
                            # The outer while loop for restart_cave will continue, and the player will reset from the beginning of the cave
                            continue
                        else:
                            restart_game = False
                            print("Thank you for playing the Adventure Game!")
                        break


                    # if open_door == 'yes':
                    #     print(BOSS*FIGHT*INTRO*BABEE)
                    #     break
                    # else:
                    #     print(RAMPAGE*YOU=DEADAF)
                    #     current_hp = 0

                else:
                    if lost_cave_input != '0':
                        print("")
                    else:
                        print("Game Over - Your health reached 0.")



            #creates the con
            restart_boss_fight = True
            if lost_cave_input != '0':
                restart_boss_fight = False
            while restart_boss_fight:
                dmg_mod = 4
                print("A single lantern dangles dingly, lighting the room dimly.")
                print("An animalistic creature paces back and forth, as if thinking about something")
                print("Realizing you are doing this for free, you decide now is as good of a time as any to call it an adventure")
                print("You look back towards the door, only to find another entrance blocked off by a massive boulder. Holding back numerous curse words, you realize the only way to get out of here is through a small hole in the wall")
                print("You make a break for the hole, not willing to fight another beast on this journey")
                print("*WOOSH*\n*THUDD*\nIt noticed you.")

                while current_hp > 0 and cm_hp > 0:
                    current_hp, cm_hp, used_potion, dmg_mod = combat_round(current_hp, armor_class, dmg_mod, cm_hp, cm_ac, cm_dmg, used_potion=False)

                if current_hp > 0:
                    print("You stand over the body of the three-headed beast, in awe of your own accomplishment")
                    print("Walking towards the exit. You feel as if you've been here before. Emerging from the ground, you find that you're in the middle of the Shrine of Good Luck")
                    print("This was a new area of the Shrine that you must have missed on your previous visit.")
                    print("In front of you are piles of arcane drawings and research documents all of which describe a creature very similar to the one you just faced.")
                    print("The documents detail the various powers the chimera posseses as well as how to best harness those powers.")
                    print("They were close too, they were only missing a way to open the seal on the cell the chimera was locked away in.")
                    print("A seal that was currently nestled deep in your traveler's bag.")
                    print("\'They were trying to \033[1mcapture\033[0m that beast\' You think to yourself")
                    print("Reading further, you discover their plans to demand power over Phandalin using the chimera for intimidation as well as to dispose of any opposition.")
                    print("Had the chimera been allowed to join their ranks, the resulting catastrophe would have been unlike the town had ever seen.")
                    print("Knowing that you had single-handedly saved the town if not the entire empire, you decide that one adventure might be enough for this year.")
                    print("Returning home, there is no fanfare, no parades down the street, in fact no one seems to acknowledge you at all.")
                    print("But their praise isn't what drove you, your sense of adventure and self-preservation almost freed the beast in the first place.")
                    print("Calling it even, you kick of your boots and lay down for a well deserved nap.")
                    input("THE END")
                    break


                if current_hp <= 0:
                    print("Bloodied and broken, you prepare to meet your end at the hands of the horrific fusion of beasts.")
                    time.sleep(4)
                    print("\nFear.\n")
                    time.sleep(3)
                    print("No longer can you feel the physical injuries littering your body, in its place is the suffocating terror of an unavoidable death.")
                    time.sleep(4)
                    print("The chimera seems to lunge in slow motion, all three of it\'s heads racing to deliver your final memory.")
                    time.sleep(4)
                    print("As your eyes close and mark the end of your short adventure, you hope at least stories of your exploits live on.")
                    time.sleep(4)
                    print("You start to feel as though you are floating. Opening your eyes, you expect to see the pearly gates, but are only greeted with an aerial view of Phandalin.")
                    time.sleep(4)
                    print("The ground beneath you explodes, the chimera lazily flying through the rubble before turning it\'s gazes upon the town.")
                    time.sleep(4)
                    print("You try to move, scream, anything to warn the townspeople of the threat just over the hill but nothing happens, you have become a hapless spectator to the inevitable carnage.")
                    time.sleep(4)
                    print("A ghost in the land of the living with an unfortunately short solitute as soon countless others will be among you.")
                    time.sleep(4)
                    print("Death itself seemed to decend upon Phandalin that day as the chimera\'s rampage was unequaled.")
                    time.sleep(4)
                    print("\n\nNone survived.\n\n")
                    time.sleep(4)
                    print("Although the townspeople tried their best to fight back, they stood no chance.")
                    time.sleep(4)

                    print("The cultists who had sought power through the chimera were not spared, and eventually they appeared amongst the rest of the late townspeople.")
                    time.sleep(4)

                    print("With nothing else to do, you decide to visit the adventurer\'s guild where your journey began hoping to get some sort of closure.")
                    time.sleep(4)

                    print("You travel through the massive double doors that mark the entrance and suddenly hear a human voice.")
                    time.sleep(3)
                    # ask player if they are ready to start
                    begin = input('"Hello Adventurer! Are you ready to begin your journey of a lifetime?" (Type Yes or No): ')  # recent change!!!!!!!!! inputs with .lower() got rid of extra "
                    # check if they typed yes or no
                    if (begin.lower() == "yes" or "no"):
                        # start
                        if (begin.lower() == "yes"):
                            print('"Wonderful! I will be your Game Master for this game. Let''s get started!"')
                        # don't start
                        elif (begin.lower() == "no"):
                            print('"Well I''m sorry to hear that. Please come again when you''re ready."')
                        # they didn't type yes or no
                        else:
                            begin = input('"I''m sorry, I don''t quite understand your answer. Can you try again?" (Type Yes or No): ')
                    # ask them if they are ready again
                    while (begin.lower() == "no"):
                        begin = input('"Are you ready to begin now?" (Type Yes or No): ')

                    break

        # # chimera hp
        # cm_hp = random.randint(12, 120) + 48
        # # chimera armor class
        # cm_ac = 14
        # # chimera damage
        # cm_dmg = random.randint(2, 12) + 4
        # # chimera fire damage
        # cm_fire = random.randint(7, 56)


        # else:
        #     print('That''s all for now')
        #     break













