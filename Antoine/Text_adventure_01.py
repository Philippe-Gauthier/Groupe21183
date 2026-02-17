"""
Text adventure game
by Antoine D-C
"""

"""
notes to self:
-
"""

#libraries
import time

#game logic
debug_delay = 0  #usually 0.5, 0 for debugging

def print_ (text, delay=debug_delay):
    print(text)
    time.sleep(delay)

#scenes

##menu
def intro():
    print_("\n\nWelcome to the Text Adventure Game!")
    name = input("What is your name, adventurer? ")
    print_(f"Hello, {name}! Your journey begins now.")
    return name

##scene 1, starting point
def scene1():

    print_("\n\nYou wake up from a deep slumber at a corner table in your local taverne.")
    print_("As you steadily regain consciousness, you notice a hooded figure sitting across from you.")
    print_("Just as you notice it, it notices you and is now rapidly approaching your table in strong, heavy strides.")
    print_("Suddently, with a rush of adrenaline, you recall what it is you went to do here today,")
    print_("It wasn't simply to get drunk, although that is an always pleasant side effect of meetings in pubs.")
    print_("Today was the day where you would finally learn who sent that letter and why it was so vague.") #if an inventory system ever gets added, here would be th point to put a "mysterious letter added to inventory" line
    print_("""Indeed, last week, you were invited to be here, at this moment, for an "opportunity". """)
    print_("The hooded stranger sits down facing you and, without warning, unsheaths a dagger, propelling it's edge towards your throat")

    time.sleep(debug_delay * 2)
    print("\n--- What do you do? ---")
    print("(1) Lean back with your entire body do try and avoid the blade")
    print("(2) Throw the table upwards to deflect the blow")
    print("(3) Nothing")
    path1 = input("What do you do? (1/2/3): ")
    return path1

##scene 1_1, lean back
def scene1_1():
    print_("\n\nYou lean back with your entire body do try and avoid the blade")
    print_("It misses you by mere inches, then, just as swiftly as it had slashed, it retracted into it's sheath.")
    print_("It all happens so fast that, for all else present, it looks only as if you had fallen to the ground from alcohol, nothing more.")
    print_("The figure stands up and offers to help you back to your feet.")
    print_(""""You are indeed as swift and insightfull as described, my time is not being wasted here". he says.""")
    print_(""""Let's talk buisness", he continues,"as you have no doubt heard, multiple adventurers have recently lost their lives climbing the mountain" """)
    print_(""""It is my belief that this, coupled with the recent unrest and growth in strenght of dark powers in the kingdom, is no coincidence." """)
    print_(""""From what I have gathered, this could be caused by the arrival of an ancient and wicked being from times long forgotten by men." """)
    print_(""""What is it?" you ask." """)
    print_(""""A foul beast, from the northern wastes, known only as the Ice Wyrm." """)
    print_(""""I, alone, cannot defeat it, that is why I come to you for aid." """)

    time.sleep(debug_delay * 2)
    print("\n--- What do you do? ---")
    print("(1) Accept")
    print("(2) Decline")
    path1_1 = input("What do you do? (1/2): ")
    return path1_1

##scene 1_1_1, accept
def scene1_1_1():
    print_("\n\nYou accept, finaly, a quest worthy of your legendary skills.")
    print_(""""We shall leave at dawn", he says, "meet me at the town gates." """)
    print_("you part ways as to not attreact attention further and go to your cottage.")
    print_("as the sun creeps over the nearby hills you make your way to the town's edge where the man awaits with horses and provisions")
    print_(""""Onwards" you enthoustiacally call once all is set." """)
    print_(""""to which path?" he anwsers,"we should decide on the road." """)
    print_(""""quite right" you say, we shall pass... """)

    time.sleep(debug_delay * 2)
    print("\n--- where will you go? ---")
    print("(1) Across the mountains, it may be perrilous but it's the fastest route")
    print("(2) Around, by the forest, it may take longer but it's safer")
    path1_1_1 = input("Where to? (1/2): ")
    return path1_1_1

##scene 1_1_1_1, across mountains
def scene1_1_1_1():
    print_("\n\nYou set off towards the mountains")
    print_("The path is easy at first, small trails often traveled by adventurers and merchants alike")
    print_("It quickly gets harsher once you step off the main roads, the paths, littered with jagged rocks and loose gravel, threaten to give way below your steps at any moment.")
    print_("the wind too picks up speed as it looses warmth, its chill soon becoming unbearable")
    print_("Just then do you reach the foot of the mountain, the path ahead of you is steep and unwelcoming, the stones replaced by even sharper icicles.")
    print_("Luckily for the both of you, you know a bit of magic from the town's artificer and you manage to conjure a small wisp of flame for the both of you")
    print_("It, combined with the heavy fur coats he brought, should be enough to keep you warm, for now")
    print_("As you reach the smallest peak, you start to be able to see beyond and it is both beautiful and terrifying")
    print_("You see the old fortress in the cold valley below, you can see the wicked beast circling the anciant bastion in the air above, it had been taken over,")

    time.sleep(debug_delay * 2)
    print("\n--- What do you do? ---")
    print("(1) descend towards the fortress")
    print("(2) setup camp and observe")
    path1_1_1_1 = input("What do you do? (1/2): ")
    return path1_1_1_1

##scene 1_1_1_1_1, descend towards the fortress
def scene1_1_1_1_1():
    print_("\n\nYou make your way down the mountain flank, carefully yet swiftly")
    print_("as you approach the fort, you can hear the beast lurking about, its evil screeches icing your soul")
    print_("you enter via a small, near invisible, service door and manage to make your way to the inner court without too much trouble")
    print_("There, you can see the Wyrm swooping down, as it lands mere meters from the pillar you hide behind, you start to appreceate how impossible a task slaying this beast will be")
    
    time.sleep(debug_delay * 2)
    print("\n--- What do you do? ---")
    print("(1) charge it down ,you have the element of surprise")
    print("(2) gather intel on the beast before attacking")
    path1_1_1_1_1 = input("What do you do? (1/2): ")
    return path1_1_1_1_1

##scene 1_1_1_1_1_1, charge it down boldly
def scene1_1_1_1_1_1():
    print_("\n\nYou both jump out from behind the pillar and run, screaming down at it")
    print_("Your companion striks first, his battle axe  smashing into the dragon's front leg, closely followed by your knives peircing a bit of its wing")
    print_("Unfortunately, its hideis to thick for the axe and it shatters upon impact and your knives are not sharp enough to slice cleanly through the wing membrane")
    print_("All this sudden violence only enrages the beast and in one movement, it throws you aside with it's powerfull taloned paws and blasts a spray of ice shards from it's mouth towards your helpless companion")
    print_("You see the storm of frosen knives shred through him like nothing, taking chunks of flesh and bones with is , in an instant, all that remains is a puddle of mangled biomass on the ground")
    print_("No time to mourn though, the dragon turns to you now, preparing another, its eyes glowing with malice")

    time.sleep(debug_delay * 2)
    print("\n--- What do you do? ---")
    print("(1) try and defend yourself with rubble lying around")
    print("(2) attack while it charges up")
    path1_1_1_1_1_1 = input("What do you do? (1/2): ")
    return path1_1_1_1_1_1

##scene 1_1_1_1_1_1_1,defend with scraps
def scene1_1_1_1_1_1_1():
    print_("\n\nYou rapidly gather all the spare, broken or loose planks of wood within reach, same with bricks and pebbles and pile them up precariously before you")
    print_("The dragon unleashes another spray of icy death in your eirectiopn and, for a small moment, the barricaade holds")
    print_("You still get disintegrated in a fine mist of blood and bones half a second later of course, but it was worth a try.")

    return int(6)

##scene 1_1_1_1_1_1_2,attack while charging     win
def scene1_1_1_1_1_1_2():
    print_("\n\nYou rapidly jump up despite the pain and draw your remaining two knives")
    print_("As the wyrm opens its mouth to spray its icy death, you land your knives directly in the roov of its mouth, mortally wounding it by cutting its brain in half from within")

    return int(6)

##scene 1_1_1_1_1_2,gather intel        open
def scene1_1_1_1_1_2():
    print_("111112")


##scene 1_1_1_1_2, setup camp and observe       open
def scene1_1_1_1_2():
    print_("11112")

##scene 1_1_1_2, through forest
def scene1_1_1_2():
    print_("\n\nYou decide to pass by the forest, this will let you go around the mountains, straight into the valley where the old fortress stands")
    print_("During the rather uneventfull begining of the trip, you talk with him to find out a little more on this quest")
    print_("He tells you that in his village, it was rumored that a dangerous demonspawn had taken refuge in these parts")
    print_("You find out this expedition is entirely based on the rambling of a half dead knight who stumbled into his village, talking about the beast")
    print_("You also find out he did a little research himself and, through tracking down travelers and adventurers, gathered enough intel to confidently say the dragon has taken over the forgotten stronghold")
    print_("About halfway througt the forest path, a group of scruffy-looking men jump out of the surrounding bushes and trees, they seem to be bandits")
    print_(""""Give us all ye got o' we gonna gut ya 'ed off " the closest one yells, pointing a small knife in your general direction""")

    time.sleep(debug_delay * 2)
    print("\n--- What do you do? ---")
    print("(1) Pay them")
    print("(2) Talk it out")
    print("(3) Make the geneva convention look like a checklist")
    path1_1_1_1 = input("What do you do? (1/2/3): ")
    return path1_1_1_1

## pay them      open
def scene1_1_1_2_1():
    print_("111121")

## talk it out       open
def scene1_1_1_2_2():
    print_("111122")

## unspeakable violence
def scene1_1_1_2_3():
    print_("\n\nYou look at youy companion, he looks back at you, you understand each other, you don't have time for this")
    print_("You then both get off your horses and while he pulls out a battle axe from his bag, you swiftly load your wrist crossbows and unsheath your daggers")
    print_(""""So, you wish to die" the bandit yells pretentiously, "Same to you" your companion calls back""")
    print_("To cut it short, let's simply say their bodies won't be found because there arent any bodies left to find.")
    print_("You then both get on your horses after having carefully looted the bodies")
    print_("you got  afew healing potions, some coins and throwing daggers from it")
    print_("you continue along the path and eventually reconvene with the other end of the mountain path, you start to be able to see the valley and it is both beautiful and terrifying")
    print_("You see the old fortress in the cold valley before you, you can see the wicked beast circling the anciant bastion in the air above, it had been taken over,")

    time.sleep(debug_delay * 2)
    print("\n--- What do you do? ---")
    print("(1) ascend towards the fortress")
    print("(2) be content with having killed bandits and head back home")
    path1_1_1_2_3 = input("What do you do? (1/2): ")
    return path1_1_1_2_3

## ascend towards the fortress      open
def scene1_1_1_2_3_1():
    print_("111231")

## head home scared
def scene1_1_1_2_3_2():
    print_("\n\nThat beast looks way too feirce, you have already rid the world of some danger today and that's enough")
    print_("you look at  your companion and both understand you're outmatched")
    print_("you take the bath back towards the town and, once there, get praised at the tavern on your exploits of the day")
    print_("another evil vanquished by you, your reputation grows, no one needs to know the whole thing")

    return int(5)

##scene 1_1_2, decline
def scene1_1_2():
    print_("\n\nYou politely decline the offer, although you may be a great adventurer, an ice wyrm is not to be trifled with.")
    print_(""""That is why I require a companion" he says,"I cannot do this alone and neither can you, but together..." """)
    print_("it is true that you have no idea of the man's skills, it may be possible and even likely that he is as capable as you are.")
    print_("the idea starts to tempt you, you imagine the glory and riches that would come from slaying such a beast.")

    time.sleep(debug_delay * 2)
    print("\n--- Do you change your mind? ---")
    print("(1) Accept")
    print("(2) Decline")
    path1_1_2 = input("What do you do? (1/2): ")
    return path1_1_2

##scene 1_1_2_1, accept     open        but will be replaced
def scene1_1_2_1():
    print_("1121")

##scene 1_1_2_2, decline
def scene1_1_2_2():
    print_("\n\nInfinite riches are useless if you're not alive to enjoy them")
    print_("""You tell him it's too dangerous and, unless he has the fabled "plot armor", you will surely die fighting the dreadfull thing" """)
    print_("You order a beer for him and leave after appologising that you could not be of any help to him")
    
    return int(3)

##scene 1_2, throw table
def scene1_2():
    print_("\n\nYou rapidly raise your knees, lunching the table upwards with all your strength.")
    print_("The blade narrowly misses your chin, your legs hit the wood with immense strength, it hurts and you're not one to leave pain unpunished.")
    print_("Taking advantage of the ensuing cahos, you spring over the tavern table, now split in two by the impact with your assailant's arms.")
    print_("Pushing him to the rough floor, punching him bloody, you pull out your own dagger and place it on his throat.")
    print_("Shouting over his struggles, you demand to know who he is and why he attacked you.")
    print_("After a long pause, the hooded figure speaks up, his voice hoarse and weak from the beating.")
    print_(""""please... not here... not now... must..." he gasps.""")
    
    time.sleep(debug_delay * 2)
    print("\n--- What do you do? ---")
    print("(1) Slowly help him up and order mead as an appology")
    print("(2) Let violence and adrenalline blind you and kill him")
    print("(3) Stop and wait")
    path1_2 = input("What do you do? (1/2/3): ")
    return path1_2

##scene 1_2_1, help him up      open
def scene1_2_1():
    print_("121")

##scene 1_2_2, kill him
def scene1_2_2():
    print_("\n\nYou can't hear his pleas over the blood pumping through you, the adrenaline and your pain blind and deafen you completely")
    print_("Violently, you decide it's not worth it to let him live, you slice his throat thrice,")
    print_("Each time comming back with more force, digging deeper in his flesh as blood spills out on the floor")
    print_("Drenching you in his warmth as he expires in your arms")
    print_("The pub is now silent, everyone either drawing their weapons or hiding under tables or behind barrels")
    print_(""""You all saw him trying to kill me, that was self-defence" you yell at them""")
    print_("Most agree out of fear, others genuinely, the bartender comes forwards cautiously ")
    print_("He asks you to leave")
    print_("You do")

    return int(2)

##scene 1_2_3, wait
def scene1_2_3():
    print_("\n\nYou unfortunately won't ever know what he meant by that, he simply dies on you")
    print_("The pub is now silent, everyone either drawing their weapons or hiding under tables or behind barrels")
    print_(""""You all saw him trying to kill me, that was self-defence" you yell at them""")
    print_("Most agree out of fear, others genuinely, the bartender comes forwards cautiously ")
    print_("He asks you to leave")
    print_("You do")

    return int(2)


##scene 1_3, do nothing
def scene1_3():
    print_("\n\nYou stand your ground, facing down death in its eyes, stoic and unflinching.")
    print_("The hooded figure stops, centimeters from your throat with a slight chuckle, it sheaths its blade and lowers its hood.")
    print_(f""""You are {name},are you not? it says.""")
    print_("You aprehenctively nod, on your guard, hand on your dagger.")
    print_(""""You are indeed as brave and insightful as described, my time is not being wasted here". he continues.""")
    print_(""""Let's talk buisness", he continues,"as you have no doubt heard, multiple adventurers have recently lost their lives climbing the mountain" """)
    print_(""""It is my belief that this, coupled with the recent unrest and growth in strenght of dark powers in the kingdom, is no coincidence." """)
    print_(""""From what I have gathered, this could be caused by the arrival of an ancient and wicked being from times long forgotten by men." """)
    print_(""""What is it?" you ask." """)
    print_(""""A foul beast, from the northern wastes, known only as the Ice Wyrm." """)
    print_(""""I, alone, cannot defeat it, that is why I come to you for aid." """)

    time.sleep(debug_delay * 2)
    print("\n--- What do you do? ---")
    print("(1) Accept")
    print("(2) Decline")
    path1_3 = input("What do you do? (1/2): ")
    return path1_3

## this is the "death screen" if you will, it prints when a path is a dead end, you made a wrong choice
def end(depth):
    print("\n________________________________")
    print(f"Your adventure ends here {name}")
    print(f"You went {depth} choices deep")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n\n")

## this prints when you finally slay the ice wyrm and win the game      open
def win(depth):
    print("\n________________________________________________________________________________________________________________________________")
    print(f"Congratulations {name}, You have killed the Ice wyrm and saved the kingdom from almost certain doom, it only took You {depth} choices.")
    print(f"You make the trip down to the village again and, after bragging about your success to the locals, go home and go to sleep.")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n\n")


#gameplay tree

name = intro()
path1 = scene1()
if path1 == "1":        #lean back
    path1_1 = scene1_1()
    if path1_1 == "1":      #accept
        path1_1_1 = scene1_1_1()
        if path1_1_1 == "1":        #across mountains
            path1_1_1_1 = scene1_1_1_1()
            if path1_1_1_1 == "1":      #descend towards the fortress
                path1_1_1_1_1 = scene1_1_1_1_1()
                if path1_1_1_1_1 == "1":        #charge it down boldly
                    path1_1_1_1_1_1 = scene1_1_1_1_1_1()
                    if path1_1_1_1_1_1 == "1":      #defend with scraps
                        end(scene1_1_1_1_1_1_1())
                    elif path1_1_1_1_1_1 == "2":        #attack while charging
                        win(scene1_1_1_1_1_1_2())
                elif path1_1_1_1_1 == "2":      #gather intel
                    scene1_1_1_1_1_2()
            elif path1_1_1_1 == "2":        #setup camp and observe
                scene1_1_1_1_2()
        elif path1_1_1 == "2":      #through forest
            path1_1_1_2 = scene1_1_1_2()
            if path1_1_1_2 == "1":      # pay them
                scene1_1_1_2_1()
            elif path1_1_1_2 == "2":    # talk it out
                scene1_1_1_2_2()
            elif path1_1_1_2 == "3":    # unspeakable violence
                path1_1_1_2_3 = scene1_1_1_2_3()
                if path1_1_1_2_3 == "1":  # ascend
                     scene1_1_1_2_3_1()
                elif path1_1_1_2_3 == "2":  # head home
                    end(scene1_1_1_2_3_2())
    elif path1_1 == "2":        #decline
        path1_1_2 = scene1_1_2()
        if path1_1_2 == "1":        #accept again
            scene1_1_2_1()         ##this choice should be replaced with the entire "Accept" path, from the if above, change before putting into 3rd path
        elif path1_1_2 == "2":      #decline again
            end(scene1_1_2_2())

elif path1 == "2":      #throw table
    path1_2 = scene1_2()
    if path1_2 == "1":      #help him up
        scene1_2_1()
    elif path1_2 == "2":        #kill him
        end(scene1_2_2())
    elif path1_2 == "3":        #wait
        end(scene1_2_3())

elif path1 == "3":      #do nothing
    path1_3 = scene1_3()
    if path1_3 == "1":       ##from this point on, it's the same as the first branche, just change the variable names to have a 3 in them, for consistency
        path1_3_1 = scene1_1_1()
        if path1_3_1 == "1":
            scene1_1_1_1()
        elif path1_3_1 == "2":
            scene1_1_1_2()
    elif path1_3 == "2":
        path1_3_2 = scene1_1_2()
        if path1_3_2 == "1":
            scene1_1_2_1()
        elif path1_3_2 == "2":
        	scene1_1_2_2()