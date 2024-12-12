import os
def main():  
    hand = False
    body = False
    knife = False
    KDW = 0
    DOH = 0
    BDM = 0
    running = True 
    while running: 
        os.system('cls')
        inputs = ['D']
        print('you stare at the crimson puddles at your feet, in your left hand is a kitchen knife and your right hand is covered in blood.')
        if not knife:
            print('>Hide Weapon: A')
            inputs.append('A')
        if not hand or KDW == 1:
            print('>Wash hands: B')
            inputs.append('B')
        if not body:
            print('>Hide body: C')
            inputs.append('C')
        print('>Run away: D')
        intake = ''
        while intake not in inputs:
            #if not hand and not body and not knife:
            #    break
            intake = input(">")
        if intake == 'A':
            knife = True
            print('>Bury it: A')
            print('>Wash it and put it back: B')
            intake = ''
            while intake not in ['A', 'B']:
                intake = input(">")
            if intake == 'A':
                print('You scrape away dirt in the garden of your backyard and carefully bury the knife.')
                input('>')
                if not hand and not body and not knife:
                    print("What's next?")
                    input('>')
                KDW = 1
                DOH = 1
            if intake == 'B':
                print('You carefully scrub the blade of the knife. The maroon hues give way to the stark silver shine of your now clean knife.')
                input('>')
                print("Once clean, you insert the knife back in its block.")
                input('>')
                if not hand and not body and not knife:
                    print("What's next?")
                    input('>')
                KDW = 2
        if intake == 'B':
            hand = True
            print("You scrub your family's blood from your hands. The sweet scent of iron permiates through the air.")
            input('>')
            if not DOH:
                print('Your hands are clean.')
                input('>')
                print("As the stench lingers, and the color fades you are left with another choice.")
                input('>')
            if DOH:
                print('You watch as the soil disolves into mud and swirls down the drain.')
                input('>')
                print('Your hands are clean.')
                input('>')
            if KDW == 1:
                KDW = 3
                DOH = 0
            else:
                DOH = 3
        if intake == 'C':
            body = True
            inputs = ['B', 'C']
            if not KDW:
                inputs.append("A")
                print('>Cut body up: A')        
            print('>Bury body: B')
            print('>Disassembly body: C')

            intake = ''
            while intake not in inputs:
                intake = input(">")
            if intake == 'A':
                print("You take your bloodied knife and cut the body apart. The sounds of slicing flesh echo in your ears as a cruel grin spreads on your lips.")
                input('>')
                print("You finish cutting up the body. And lick your lips of a stray blood drop. Delicious...")
                input('>')
                BDM = 1
            if intake == 'B':
                print("You go into your shed and grab your spade. You quickly dig up a hole and toss in the corpse. The body makes a dull thud as it lands.")
                input('>')
                print("After covering the aftermath of your most recent murder with dirt, you scatter some leaves across the disturbted soil.")
                input('>')
                print("...It looks fine.")
                input('>')
                DOH = 1
                BDM = 2
            if intake == 'C':
                print("Without a knife to cut the body apart, you're left alone with just your hands. You know what you have to do.")
                input('>')
                print('You set to work tearing apart your victim, limb after bloodied limb.')
                input('>')
                print("It  isn't pretty but... something about rending a person to shreds, raw and by your own hands fills you with a sickening thrill. It's... exhilerating.")
                input('>')
                print("You finally take the lacerated and mangled corpse and bury it. The tattered flesh and butchered bones make it easy to dispose.")
                input('>')
                BDM = 3
        if intake == 'D':
            running = False
            if (KDW == 3 or KDW == 1) and BDM == 2:#ending 1
                print("The disheveled piles of dirt in your backyard result in a dead giveaway (pun intended).")
                input('>')
                print("You get caught.")
                input('>')
                print("(So much for touching grass...)")
            elif KDW == 2 and BDM == 2:#ending 2
                print("You tell the cops that you buried your loved one in your family graveyard.")
                input('>')
                print("Without a weapon to prove a murder, you manage to get away with innocence.")
                input('>')
                print("(How big is your backyard??)")
            elif BDM == 3 and (KDW == 1 or KDW == 3):#ending 3
                print("In the rush of burying and tearing apart the body, you seem to have missed a few shreds of sinew.")
                input('>')
                print("The cops trace the evidence back to you and you get caught.")
                input('>')
                print("(Idiot.)")
            elif BDM == 3 and KDW == 2:#ending 4
                print("After masterfully disposing of the body and hiding the knife, the cops find nothing")
                input('>')
                print("You get away scott free.")
                input('>')
                print("(Put you can't seem to shake the feeling of tearing the person part. In fact, you seem to crave it again.)")
            elif BDM == 1 and (KDW == 1  or KDW == 3):#ending 5
                print("After cutting apart the corpse, You decide you use some of the meat to make yourself a snack.")
                input('>')
                print("But without a knife to work with anymore, its hard to tear apart the flesh.")
                input('>')
                print("You are caught with your mouth full.")
                input('>')
                print("(Unfortunately, the flesh is not cherry flavored)")
            elif KDW == 2 and BDM == 1:#ending 6
                print("You store the pieces of human flesh in your fridge and begin to make yourself dinner.")
                input('>')
                print("Not only is your fridge stocked, but you manage to get away as well.")
                input('>')
                print("(Let him cook!)")
            else:
                if not body and not knife:
                    print("You run off leaving all the evidence behind.")
                    input('>')
                    print("You get caught.")
                    input('>')
                    if not hand:#dirty hands
                        print("As you're being dragged to the police car, you look down at your filthy ahh- hands")
                        input('>')
                        print("(gross)")
                    else:
                        print("(What did you expect?)")
                elif not body:#not dealt with body
                    print("With the knife gone, you take one last look at your victim before dashing out the door.")
                    input('>')
                    print("You run into a police officer and manage to stutter out something close to an excuse.")
                    input('>')
                    if not hand:#dirty hands
                        print("You look down at your still bloodied hands and hope that won't come back to bite you.")
                        input('>')
                        print("It did. The police trace the finger prints back to you. You get caught.")
                        input('>')
                        print("(you probably shoulda washed your hands)")
                    else:
                        print("Somehow your excuse worked!")
                        input('>')
                        print("The police tell you to move along. And you get away.")
                        input('>')
                        print("(Lucky...)")
                elif not knife:#not dealt with knife
                    print("You take the knife with you as you run.")
                    input('>')
                    print("You get away, and with your new found hobby you quickly become a well known serial killer and local cryptid.")
                    input('>')
                    print("(Mothman does not approve.)")
                
if __name__ == "__main__":
    main()