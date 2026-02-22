"""
Text adventure game
by Antoine D-C
"""

"""
notes to self:
-Capitalise all start of line in text, for consistency, also make sure the \n are in the right place
"""

#libraries
import time
from termcolor import colored, cprint 

#tells the game if you are debugging it or not, 1 = debug, 0 = intended experience
debug_mode = 1

#game logic
default_text_color = "white"
text_color = default_text_color
path_length = 0

def delay():
    """
    this function handles the delay between prints, it looks wether the game is in debug mode or not and ajusts the delay accordingly.
    when debug mode is active, no delay is set, when not, it has the text wait 0.5 sec between each line 
    """
    global debug_mode
    if debug_mode < 1:
        return float(0.5)
    else:
        return int(0)
    
def print_ (text):
    """
    This code is for adding dramatic delay to the thext display,
    it's used exactly as a print would since the delay is already preset by the debug_delay elsewhere,
    it can also change the text color like a normal print, though this one is decided by the text_color variable
    """
    color = text_color
    scroll_delay = delay()
    print(colored(text, color))
    time.sleep(scroll_delay)

def ans(amnt, question):
    """
    This function deals with the path choices, it takes the amount of possible choices and the question that needs to be asked,
    it then checks wether the choice the user made is valid, if so, it returns that choice to be used in the tree,
    if not, it asks again while displaying an error message
    """
    while True:
        try:
            choice = int(input(colored(question, "green")))
            if 1 <= choice <= amnt:
                return str(choice)
            else:
                cprint("\nInvalid choice, please choose again\n", "red", attrs=["bold"])
        except ValueError:
            cprint("\nInvalid input, please enter a number\n", "red", attrs=["bold"])

def color_change(color):
    """
    this function changes the color of the text that will be displayed afterwards
    """
    global text_color
    text_color = color


#scenes
"""
All the "functions" below work similarly, they're just the different scenes , or "pages of the book"
they have no parameters since they are not meant to threat data but store "pages" and return the user's choice.
Some return int values, they're for branch ends, others return strings, they're the choices.
The first one starts the adventure, it return the user's name to be used and displayed elsewhere.
The last two ones are the actually ends of the paths, they take an int, represrenting how many choices the user made, and display their name and nb of choices made in a text
"""

##menu
def intro():
    color_change("green")
    print_("\n\nWelcome to the Text Adventure Game!")
    name = input(colored("What is your name, adventurer? ", text_color))
    print_(f"Hello, {name}! Your journey begins now.")
    color_change(default_text_color)
    return name

##scene 1, starting point
def scene1():
    global path_length
    path_length = path_length + 1
    print_("\n\nYou wake up from a deep slumber at a corner table in your local taverne.")
    print_("As you steadily regain consciousness, you notice a hooded figure sitting across from you.")
    print_("Just as you notice it, it notices you and is now rapidly approaching your table in strong, heavy strides.")
    print_("Suddently, with a rush of adrenaline, you recall what it is you went to do here today,")
    print_("It wasn't simply to get drunk, although that is an always pleasant side effect of meetings in pubs.")
    print_("Today was the day where you would finally learn who sent that letter and why it was so vague.") #if an inventory system ever gets added, here would be th point to put a "mysterious letter added to inventory" line
    print_("""Indeed, last week, you were invited to be here, at this moment, for an "opportunity". """)
    print_("The hooded stranger sits down facing you and, without warning, unsheaths a dagger, propelling it's edge towards your throat")

    time.sleep(delay() * 2)
    print("\n--- What do you do? ---")
    print("(1) Lean back with your entire body do try and avoid the blade")
    print("(2) Throw the table upwards to deflect the blow")
    print("(3) Nothing")
    return ans(3, "What do you do? (1/2/3): ")

##scene 1_1, lean back
def scene1_1():
    global path_length
    path_length = path_length + 1
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

    time.sleep(delay() * 2)
    print("\n--- What do you do? ---")
    print("(1) Accept")
    print("(2) Decline")
    return ans(2, "What do you do? (1/2): ")

##scene 1_1_1, accept
def scene1_1_1():
    global path_length
    path_length = path_length + 1
    print_("\n\nYou accept, finaly, a quest worthy of your legendary skills.")
    print_(""""We shall leave at dawn", he says, "meet me at the town gates." """)
    print_("you part ways as to not attreact attention further and go to your cottage.")
    print_("as the sun creeps over the nearby hills you make your way to the town's edge where the man awaits with horses and provisions")
    print_(""""Onwards" you enthoustiacally call once all is set." """)
    print_(""""to which path?" he anwsers,"we should decide on the road." """)
    print_(""""quite right" you say, we shall pass... """)

    time.sleep(delay() * 2)
    print("\n--- where will you go? ---")
    print("(1) Across the mountains, it may be perrilous but it's the fastest route")
    print("(2) Around, by the forest, it may take longer but it's safer")
    return ans(2, "Where to? (1/2): ")

##scene 1_1_1_1, across mountains
def scene1_1_1_1():
    global path_length
    path_length = path_length + 1
    print_("\n\nYou set off towards the mountains")
    print_("The path is easy at first, small trails often traveled by adventurers and merchants alike")
    print_("It quickly gets harsher once you step off the main roads, the paths, littered with jagged rocks and loose gravel, threaten to give way below your steps at any moment.")
    print_("the wind too picks up speed as it looses warmth, its chill soon becoming unbearable")
    print_("Just then do you reach the foot of the mountain, the path ahead of you is steep and unwelcoming, the stones replaced by even sharper icicles.")
    print_("Luckily for the both of you, you know a bit of magic from the town's artificer and you manage to conjure a small wisp of flame for the both of you")
    print_("It, combined with the heavy fur coats he brought, should be enough to keep you warm, for now")
    print_("As you reach the smallest peak, you start to be able to see beyond and it is both beautiful and terrifying")
    print_("You see the old fortress in the cold valley below, you can see the wicked beast circling the anciant bastion in the air above, it had been taken over,")

    time.sleep(delay() * 2)
    print("\n--- What do you do? ---")
    print("(1) descend towards the fortress")
    print("(2) setup camp and observe")
    return ans(2, "What do you do? (1/2): ")

##scene 1_1_1_1_1, descend towards the fortress
def scene1_1_1_1_1():
    global path_length
    path_length = path_length + 1
    print_("\n\nYou make your way down the mountain flank, carefully yet swiftly")
    print_("as you approach the fort, you can hear the beast lurking about, its evil screeches icing your soul")
    print_("you enter via a small, near invisible, service door and manage to make your way to the inner court without too much trouble")
    print_("There, you can see the Wyrm swooping down, as it lands mere meters from the pillar you hide behind, you start to appreceate how impossible a task slaying this beast will be")
    
    time.sleep(delay() * 2)
    print("\n--- What do you do? ---")
    print("(1) charge it down ,you have the element of surprise")
    print("(2) gather intel on the beast before attacking")
    return ans(2, "What do you do? (1/2): ")

##scene 1_1_1_1_1_1, charge it down boldly
def scene1_1_1_1_1_1():
    global path_length
    path_length = path_length + 1
    print_("\n\nYou both jump out from behind the pillar and run, screaming down at it")
    print_("Your companion striks first, his battle axe  smashing into the dragon's front leg, closely followed by your knives peircing a bit of its wing")
    print_("Unfortunately, its hideis to thick for the axe and it shatters upon impact and your knives are not sharp enough to slice cleanly through the wing membrane")
    print_("All this sudden violence only enrages the beast and in one movement, it throws you aside with its powerfull taloned paws and blasts a spray of ice shards from it's mouth towards your helpless companion")
    print_("You see the storm of frosen knives shred through him like nothing, taking chunks of flesh and bones with it, in an instant, all that remains is a puddle of mangled biomass on the ground")
    print_("No time to mourn though, the dragon turns to you now, preparing another, its eyes glowing with malice")

    time.sleep(delay() * 2)
    print("\n--- What do you do? ---")
    print("(1) try and defend yourself with rubble lying around")
    print("(2) attack while it charges up")
    return ans(2, "What do you do? (1/2): ")

##scene 1_1_1_1_1_1_1,defend with scraps        end
def scene1_1_1_1_1_1_1():
    global path_length
    print_("\n\nYou rapidly gather all the spare, broken or loose planks of wood within reach, same with bricks and pebbles and pile them up precariously before you")
    print_("The dragon unleashes another spray of icy death in your direction and, for a small moment, the barricaade holds")
    print_("You still get disintegrated in a fine mist of blood and bones half a second later of course, but it was worth a try.")

    return path_length

##scene 1_1_1_1_1_1_2,attack while charging     win
def scene1_1_1_1_1_1_2():
    global path_length
    print_("\n\nYou rapidly jump up despite the pain and draw your remaining two knives")
    print_("As the wyrm opens its mouth to spray its icy death, you land your knives directly in the roov of its mouth, mortally wounding it by cutting its brain in half from within")

    return path_length

##scene 1_1_1_1_1_2,gather intel        win
def scene1_1_1_1_1_2():
    global path_length
    print_("\n\nYou wait and observe the beast, trying to find a flaw to expliot")
    print_("it takes a while but you notice that a few scales are missing in th center of its chest, probably a mark left by another adventurer who failed to do what you are currently attempting")
    print_("""You take your chance and while yelling "distract it's head!!" to your companion, you pull out your daggers and jump for the heart if the wyrm""")
    print_("While the dragon charges down its bait, you land the blades squarely in its hears, the cursed beast writhes in agony for a few minutes, thrashing around its limbs")

    return path_length

##scene 1_1_1_1_2, setup camp and observe
def scene1_1_1_1_2():
    global path_length
    path_length = path_length + 1
    print_("\n\nYou set up camp and observe the dragon fly around its lair")
    print_("before long, the light from your wisp alerts the beast to your location and it starts rapidly approaching the awkward camp you made")
    print_("It looks like you will need to fight it here, it's not ideal but you have no choice")
    print_("the wyrm is finally within range, you shoot your two small wrist crossbows at it, they miss, you only turned its curiosity into anger")
    print_("The dragon then lets out a blood chilling roar and blasts a spray of ice shards from it's mouth towards your helpless companion")
    print_("You see the storm of frosen knives shred through him like nothing, taking chunks of flesh and bones with it, in an instant, all that remains is a puddle of mangled biomass on the ground")
    print_("No time to mourn though, the dragon turns to you now, preparing another, its eyes glowing with malice")

    time.sleep(delay() * 2)
    print("\n--- What do you do? ---")
    print("(1) try and hide beheind a rock")
    print("(2) reload and attempt to shoot it again")
    return ans(2, "What do you do? (1/2): ")

##scene 1_1_1_1_2_1, hide behind rock
def scene1_1_1_1_2_1():
    global path_length
    path_length = path_length + 1
    print_("\n\nYou hide behind a nearby rock and pray the dragon doesn't fly around to face you")
    print_("It doesn't, but it still sprays at you, the rock holds")
    print_("You emerge from your hiding spot, having had time to reload your crossbows, you notice the face of the stone has been reduced to gravel by the ice blast")
    print_("You take aim and, as you are about to fire, you see a small patch of broken scales near the beast's heart, probably a mark left by another adventurer who failed to do what you are currently attempting")

    time.sleep(delay() * 2)
    print("\n--- What do you do? ---")
    print("(1) wait for it to land and attempt to strike it with your daggers")
    print("(2) aim for the bare skin")
    return ans(2, "What do you do? (1/2): ")

## scene1_1_1_1_2_1_1, wait for landing         end
def  scene1_1_1_1_2_1_1():
    global path_length
    print_("\n\nYou wait for the beast to land")
    print_("At some point it seems to be swooping down for it but you were wrong, it actually just starts to attack you with its powerfull taloned paws")
    print_("You dodge them all at first but after a few passes, one talon you couldn't see opens a huge gaping wound in your back")
    print_("You feel your blood pour out of your veins and cascade down your legs")
    print_("you die")

    return path_length

## scene1_1_1_1_2_1_2, shoot crossbow       win
def scene1_1_1_1_2_1_2():
    global path_length
    print_("\n\nYou aim and shoot as it swoops down to attack with its powerfull taloned paws")
    print_("Both your arrows land, the wyrm crashes out of the air and writhes in agony for a few minutes, thrashing around its limbs")

    return path_length

##scene 1_1_1_1_2_2, reload crossbows       end
def scene1_1_1_1_2_2():
    global path_length
    print_("\n\nYou reach for your spare arrows and rapidly reload your crossbows but it's too late")
    print_("The dragon unleashes another spray of icy death in your direction")
    print_("You get disintegrated in a fine mist of blood and bones half a second later, but it was worth a try.")

    return path_length

##scene 1_1_1_2, through forest
def scene1_1_1_2():
    global path_length
    path_length = path_length + 1
    print_("\n\nYou decide to pass by the forest, this will let you go around the mountains, straight into the valley where the old fortress stands")
    print_("During the rather uneventfull begining of the trip, you talk with him to find out a little more on this quest")
    print_("He tells you that in his village, it was rumored that a dangerous demonspawn had taken refuge in these parts")
    print_("You find out this expedition is entirely based on the rambling of a half dead knight who stumbled into his village, talking about the beast")
    print_("You also find out he did a little research himself and, through tracking down travelers and adventurers, gathered enough intel to confidently say the dragon has taken over the forgotten stronghold")
    print_("About halfway througt the forest path, a group of scruffy-looking men jump out of the surrounding bushes and trees, they seem to be bandits")
    print_(""""Give us all ye got o' we gonna gut ya 'ed off " the closest one yells, pointing a small knife in your general direction""")

    time.sleep(delay() * 2)
    print("\n--- What do you do? ---")
    print("(1) Pay them")
    print("(2) Talk it out")
    print("(3) Make the geneva convention look like a checklist")
    return ans(3, "What do you do? (1/2/3): ")

##scene1_1_1_2_1, pay them
def scene1_1_1_2_1():
    global path_length
    path_length = path_length + 1
    print_("\n\nYou pay them the contents of your pouch and tell them it's all you have ")
    print_("Since the pouch was filled pretty subtancially, they seem content with the transaction and agree to let you pass")
    print_("you continue along the path and eventually reconvene with the other end of the mountain path, you start to be able to see the valley and it is both beautiful and terrifying")
    print_("You see the old fortress in the cold valley before you, you can see the wicked beast circling the anciant bastion in the air above, it had been taken over,")
    print_("The wyrm looks absolutely terrifying and for the first time, you realise how impossible the task may be")

    time.sleep(delay() * 2)
    print("\n--- What do you do? ---")
    print("(1) Ascend towards the fortress")
    print("(2) Head home, you would certainly die")
    return ans(2, "What do you do? (1/2): ")

##scene1_1_1_2_1_1, ascend to fort
def scene1_1_1_2_1_1():
    global path_length
    path_length = path_length + 1
    print_("\n\nYou make your way up the valley, carefully yet swiftly")
    print_("as you approach the fort, you can hear the beast lurking about, its evil screeches icing your soul")
    print_("you enter via a small, near invisible, service door and manage to make your way to the inner court without too much trouble")
    print_("There, you can see the Wyrm swooping down, as it lands mere meters from the pillar you hide behind, you start to appreceate how impossible a task slaying this beast will be")
    
    time.sleep(delay() * 2)
    print("\n--- What do you do? ---")
    print("(1) charge it down ,you have the element of surprise")
    print("(2) gather intel on the beast before attacking")
    return ans(2, "What do you do? (1/2): ")

##scene1_1_1_2_1_2, head home       end
def scene1_1_1_2_1_2():
    global path_length
    print_("\n\nThat beast looks way too feirce, you have already rid the world of some danger today and that's enough")
    print_("you look at  your companion and both understand you're outmatched")
    print_("What a waste of time")

    return path_length

##scene1_1_1_2_2, talk it out       end
def scene1_1_1_2_2():
    global path_length
    print_("""\n\n"Now now" you say "what could we possibly have to offer to distinguished gents such as yourselves" """)
    print_(""""Well ya look like ye could pe'haps be a lil 'eavy fo' travel, it aint so much about wa' we need so much as wa' ye don't if ye ge' wa' i'm sayn' " he says""")
    print_(""""I see" you say, "well in that case, learn that we have packed only the strict minimmum for our voyage, we could not forsee letting go of anything" """)
    print_(""""Real shame tha' is" he says"we still gonna need somtin' fo' our trouble" """)
    print_("with that, the whole gang jumps out at you and, while you and your companion do react fast enough, you could not forsee the fact that they had blowguns ")
    print_("A bandid which stayed hidden in the small nearby stream shoots a poison dart to your necks and you both fall, dead")
    print_("They loot your corps and, a few months later, perish as the wyrm rampages the region")

    return path_length

##scene1_1_1_2_3, unspeakable violence
def scene1_1_1_2_3():
    global path_length
    path_length = path_length + 1
    print_("\n\nYou look at youy companion, he looks back at you, you understand each other, you don't have time for this")
    print_("You then both get off your horses and while he pulls out a battle axe from his bag, you swiftly load your wrist crossbows and unsheath your daggers")
    print_(""""So, you wish to die" the bandit yells pretentiously, "Same to you" your companion calls back""")
    print_("To cut it short, let's simply say their bodies won't be found because there arent any bodies left to find.")
    print_("You then both get on your horses after having carefully looted the bodies")
    print_("you got  afew healing potions, some coins and throwing daggers from it")
    print_("you continue along the path and eventually reconvene with the other end of the mountain path, you start to be able to see the valley and it is both beautiful and terrifying")
    print_("You see the old fortress in the cold valley before you, you can see the wicked beast circling the anciant bastion in the air above, it had been taken over,")

    time.sleep(delay() * 2)
    print("\n--- What do you do? ---")
    print("(1) ascend towards the fortress")
    print("(2) be content with having killed bandits and head back home")
    return ans(2, "What do you do? (1/2): ")

##scene1_1_1_2_3_1, ascend towards the fortress
def scene1_1_1_2_3_1():
    global path_length
    path_length = path_length + 1
    print_("\n\nYou make your way up the valley, carefully yet swiftly")
    print_("as you approach the fort, you can hear the beast lurking about, its evil screeches icing your soul")
    print_("you enter via a small, near invisible, service door and manage to make your way to the inner court without too much trouble")
    print_("There, you can see the Wyrm swooping down, as it lands mere meters from the pillar you hide behind, you start to appreceate how impossible a task slaying this beast will be")
    
    time.sleep(delay() * 2)
    print("\n--- What do you do? ---")
    print("(1) charge it down ,you have the element of surprise")
    print("(2) gather intel on the beast before attacking")
    return ans(2, "What do you do? (1/2): ")

##scene1_1_1_2_3_2, head home scared     end
def scene1_1_1_2_3_2():
    global path_length
    print_("\n\nThat beast looks way too feirce, you have already rid the world of some danger today and that's enough")
    print_("you look at  your companion and both understand you're outmatched")
    print_("you take the bath back towards the town and, once there, get praised at the tavern on your exploits of the day")
    print_("another evil vanquished by you, your reputation grows, no one needs to know the whole thing")

    return path_length

##scene 1_1_2, decline
def scene1_1_2():
    global path_length
    path_length = path_length + 1
    print_("\n\nYou politely decline the offer, although you may be a great adventurer, an ice wyrm is not to be trifled with.")
    print_(""""That is why I require a companion" he says,"I cannot do this alone and neither can you, but together..." """)
    print_("it is true that you have no idea of the man's skills, it may be possible and even likely that he is as capable as you are.")
    print_("the idea starts to tempt you, you imagine the glory and riches that would come from slaying such a beast.")

    time.sleep(delay() * 2)
    print("\n--- Do you change your mind? ---")
    print("(1) Accept")
    print("(2) Decline")
    return ans(2, "What do you do? (1/2): ")

##scene 1_1_2_2, decline again       end
def scene1_1_2_2():
    global path_length
    print_("\n\nInfinite riches are useless if you're not alive to enjoy them")
    print_("""You tell him it's too dangerous and, unless he has the fabled "plot armor", you will surely die fighting the dreadfull thing" """)
    print_("You order a beer for him and leave after appologising that you could not be of any help to him")
    
    return path_length

##scene 1_2, throw table
def scene1_2():
    global path_length
    path_length = path_length + 1
    print_("\n\nYou rapidly raise your knees, lunching the table upwards with all your strength.")
    print_("The blade narrowly misses your chin, your legs hit the wood with immense strength, it hurts and you're not one to leave pain unpunished.")
    print_("Taking advantage of the ensuing cahos, you spring over the tavern table, now split in two by the impact with your assailant's arms.")
    print_("Pushing him to the rough floor, punching him bloody, you pull out your own dagger and place it on his throat.")
    print_("Shouting over his struggles, you demand to know who he is and why he attacked you.")
    print_("After a long pause, the hooded figure speaks up, his voice hoarse and weak from the beating.")
    print_(""""please... not here... not now... must..." he gasps.""")
    
    time.sleep(delay() * 2)
    print("\n--- What do you do? ---")
    print("(1) Slowly help him up and order mead as an appology")
    print("(2) Let violence and adrenalline blind you and kill him")
    print("(3) Stop and wait")
    return ans(3, "What do you do? (1/2/3): ")

##scene 1_2_1, help him up
def scene1_2_1():
    global path_length
    path_length = path_length + 1
    print_("\n\nYou help him get up, while he sits back down, you order two pints and tell him you're listening")
    print_("""He starts: "as you have no doubt heard, multiple adventurers have recently lost their lives climbing the mountain" """)
    print_(""""It is my belief that this, coupled with the recent unrest and growth in strenght of dark powers in the kingdom, is no coincidence." """)
    print_(""""From what I have gathered, this could be caused by the arrival of an ancient and wicked being from times long forgotten by men." """)
    print_(""""What is it?" you ask." """)
    print_(""""A foul beast, from the northern wastes, known only as the Ice Wyrm." """)
    print_(""""I, alone, cannot defeat it, that is why I come to you for aid." """)
    
    
    time.sleep(delay() * 2)
    print("\n--- What do you do? ---")
    print("(1) Accept")
    print("(2) Decline")
    return ans(2, "What do you do? (1/2): ")

##scene 1_2_1_1, Accept
def scene1_2_1_1():
    global path_length
    path_length = path_length + 1
    print_("\n\nYou accept, finaly, a quest worthy of your legendary skills.")
    print_("You start to discuss the details of the endavour, he says he has all the necessary gear to leave at first light")
    print_("You would normally accept but all this talking makes you remember about the town's wizzard, maybe he could help.")
    print_("He agrees to see him and so you both leave the taverne")
    print_("during the walk, you support him so he doesn't fall over, the injuries are still fresh after all")
    print_("Once at the wizzard's tower, you knock, wait, knock again, finally, the door opens")
    print_("An old bearded man appears before you both")
    print_(f""""Ah, yes, {name}, come in, I've been expecting you both" """)
    print_(""""I Know why you are here" he says "And I can help you" """)
    print_(""""that's great" you say "so how do we kill this thing?" """)
    print_(""""I have a powerfull spell you see, one that can kill any demon, from anywhere. One problem though is that it requiers a sacrifice" """)
    print_(""""One of you will neeed to die for the demon to be banished" """)

    time.sleep(delay() * 2)
    print("\n--- What do you do? ---")
    print("(1) Sacrifice yourself")
    print("(2) Sacrifice your companion")
    print("(3) Go fetch someone to be sacrificed")
    return ans(3, "What do you do? (1/2/3): ")

##scene 1_2_1_1_1, kys      end
def scene1_2_1_1_1():
    global path_length
    print_("\n\nYou propose yourself as payment for the spell")
    print_(""""Very well" the wizzard says, "We shall need your heart, please lay down" """)
    print_("You do, he pulls out a glowing dagger and plunges it trough your chest")
    print_("You die in atrocious agony while you faintly hear him chant in an unknown language")
    print_("You will never know if the spell worked")

    return path_length

##scene 1_2_1_1_2, kill companion
def scene1_2_1_1_2():
    global path_length
    path_length = path_length + 1
    print_("\n\nYou propose that, since this was his quest, it should be him who needs to die")
    print_("He refuses, understandably, so you pull out your dagger and ask again, saying you don't really want to die today")
    print_("He pulls out his axe from his belt and replies the same")
    print_("he charges at you")
    
    time.sleep(delay() * 2)
    print("\n--- What do you do? ---")
    print("(1) Parry")
    print("(2) Dodge")
    return ans(2, "What do you do? (1/2): ")

##scene 1_2_1_1_2_1, parry      end
def scene1_2_1_1_2_1():
    global path_length
    print_("\n\nYou parry his attack and, while he lifts the axe again, attempt to strike his throat")
    print_("unfortunately, he steps back and before you can turn around, loges his axe in your spine")
    print("You fall to the ground and you can faintly see the wizard unsheathing a glowing dagger, you feel it plunging trough your chest")
    print_("You die in atrocious agony while you faintly hear him chant in an unknown language")
    print_("You will never know if the spell worked")

    return path_length

##scene 1_2_1_1_2_2, parry      win
def scene1_2_1_1_2_2():
    global path_length
    print_("\n\nYou step ideways and , as the follow-through carries him forwards, you slice his throat")
    print_("The wizzard pulls out a glowing dagger and plunges it trough his chest")
    print_("He pulls out your companion's heart, chanting in an unknown language")
    print_("The heart suddently bursts in flame and vanishes in ash")
    print_(""""That's it" the wizzard says "The wyrm's dead, take half of what your freind had on him and go home, the other half will be my payment" """)
    print_("You do as he said")

    return path_length

##scene 1_2_1_1_3, sac stranger         win
def scene1_2_1_1_3():
    global path_length
    print_("\n\nThere's no way you would die for something like that, you then decide to look for an innocent soul to take instead")
    print_("""You both make your way to the city hall and ask the high judge if the wizzard could "borrow" a criminal who would otherwise be headed for a public execution""")
    print_(""""Good heavens No!" he says"What an atrocious demand! you'd be lucky that I don't have you arrested for even thinking that" """)
    print_("You then explain the situation, how this sacrifice would save the town by killing the demon that had taken home just on the other flank of the mountain")
    print_(""""Well..." he said uneasily "i do owe that old wizzard something, and it would be better for all of us... but not a word of it, do you understand!" """)
    print_("""One hour later, you return to the tower with a prisoner, the wizzard gives you all a drink "as a welcome gift" and the prisoner falls asleep almost instantly""")
    print_("you lay him on an altar and prisoner the wizzard pulls out a glowing dagger and plunges it trough his chest")
    print_("He pulls out your companion's heart, chanting in an unknown language")
    print_("The heart suddently bursts in flame and vanishes in ash")
    print_(""""That's it" the wizzard says "The wyrm's dead, go home, you'll pay me later" """)
    print_("You do as he said")

    return path_length

##scene 1_2_2, kill him     end
def scene1_2_2():
    global path_length
    print_("\n\nYou can't hear his pleas over the blood pumping through you, the adrenaline and your pain blind and deafen you completely")
    print_("Violently, you decide it's not worth it to let him live, you slice his throat thrice,")
    print_("Each time comming back with more force, digging deeper in his flesh as blood spills out on the floor")
    print_("Drenching you in his warmth as he expires in your arms")
    print_("The pub is now silent, everyone either drawing their weapons or hiding under tables or behind barrels")
    print_(""""You all saw him trying to kill me, that was self-defence" you yell at them""")
    print_("Most agree out of fear, others genuinely, the bartender comes forwards cautiously ")
    print_("He asks you to leave")
    print_("You do")

    return path_length

##scene 1_2_3, wait     end
def scene1_2_3():
    global path_length
    print_("\n\nYou unfortunately won't ever know what he meant by that, he simply dies on you")
    print_("The pub is now silent, everyone either drawing their weapons or hiding under tables or behind barrels")
    print_(""""You all saw him trying to kill me, that was self-defence" you yell at them""")
    print_("Most agree out of fear, others genuinely, the bartender comes forwards cautiously ")
    print_("He asks you to leave")
    print_("You do")

    return path_length

##scene 1_3, do nothing
def scene1_3():
    global path_length
    path_length = path_length + 1
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

    time.sleep(delay() * 2)
    print("\n--- What do you do? ---")
    print("(1) Accept")
    print("(2) Decline")
    return ans(2, "What do you do? (1/2): ")

## this is the "death screen" if you will, it prints when a path is a dead end, you made a wrong choice
def end(depth):
    color_change("blue")
    print(colored("\n________________________________", text_color))
    print(colored(f"Your adventure ends here {name}", text_color))
    print(colored(f"You went {depth} choices deep", text_color))
    print(colored("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n\n", text_color))
    color_change(default_text_color)

## this prints when you finally slay the ice wyrm and win the game
def win(depth):
    color_change("blue")
    print(colored("\n________________________________________________________________________________________________________________________________", text_color))
    print(colored(f"Congratulations {name}, You have killed the Ice wyrm and saved the kingdom from almost certain doom, it only took You {depth} choices.", text_color))
    print(colored(f"You make the trip down to the village again and, after bragging about your success to the locals, go home and go to sleep.", text_color))
    print(colored("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n\n", text_color))
    color_change(default_text_color)

## this prints when you use the ritual to kill the ice wyrm and win the game
def win2(depth):
    color_change("blue")
    print(colored("\n________________________________________________________________________________________________________________________________", text_color))
    print(colored(f"Congratulations {name}, You have killed the Ice wyrm and saved the kingdom from almost certain doom, it only took You {depth} choices.", text_color))
    print(colored(f"Several days later, you hear a group of travelers recounting how, while they were just fighting a dragon in the mountains, it suddently drop dead", text_color))    
    print(colored(f"You take it to mean the spell worked, even though it itches you how you can hardly claim to be the one to have done it", text_color))
    print(colored("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n\n", text_color))
    color_change(default_text_color)


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
                    win(scene1_1_1_1_1_2())
            elif path1_1_1_1 == "2":        #setup camp and observe
                path1_1_1_1_2 = scene1_1_1_1_2()
                if path1_1_1_1_2 == "1":        #hide behind rock
                    path1_1_1_1_2_1 = scene1_1_1_1_2_1()
                    if  path1_1_1_1_2_1 == "1":     #wait for landing
                         end(scene1_1_1_1_2_1_1())
                    elif path1_1_1_1_2_1 == "2":        #shoot crossbows
                        win(scene1_1_1_1_2_1_2())
                elif path1_1_1_1_2 == "2":      #reload crossbows
                    end(scene1_1_1_1_2_2())
        elif path1_1_1 == "2":      #through forest
            path1_1_1_2 = scene1_1_1_2()
            if path1_1_1_2 == "1":      # pay them
                path1_1_1_2_1 = scene1_1_1_2_1()
                if path1_1_1_2_1 == "1":        #ascend to fort
                    path1_1_1_2_1_1 = scene1_1_1_2_1_1()
                    if path1_1_1_2_1_1 == "1":        #charge it down boldly
                        path1_1_1_2_1_1_1 = scene1_1_1_1_1_1()
                        if path1_1_1_2_1_1_1 == "1":      #defend with scraps
                            end(scene1_1_1_1_1_1_1())
                        elif path1_1_1_2_1_1_1 == "2":        #attack while charging
                            win(scene1_1_1_1_1_1_2())
                    elif path1_1_1_2_1_1 == "2":      #gather intel
                        win(scene1_1_1_1_1_2())
                elif path1_1_1_2_1 == "2":      #head home
                    end(scene1_1_1_2_1_2())
            elif path1_1_1_2 == "2":    # talk it out
                end(scene1_1_1_2_2())
            elif path1_1_1_2 == "3":    # unspeakable violence
                path1_1_1_2_3 = scene1_1_1_2_3()
                if path1_1_1_2_3 == "1":        # ascend
                    path1_1_1_2_3_1 = scene1_1_1_2_3_1()
                    if path1_1_1_2_3_1 == "1":        #charge it down boldly
                        path1_1_1_2_3_1_1 = scene1_1_1_1_1_1()
                        if path1_1_1_2_3_1_1 == "1":      #defend with scraps
                            end(scene1_1_1_1_1_1_1())
                        elif path1_1_1_2_3_1_1 == "2":        #attack while charging
                            win(scene1_1_1_1_1_1_2())
                    elif path1_1_1_2_3_1 == "2":      #gather intel
                        win(scene1_1_1_1_1_2())
                elif path1_1_1_2_3 == "2":     # head home
                    end(scene1_1_1_2_3_2())
    elif path1_1 == "2":        #decline
        path1_1_2 = scene1_1_2()
        if path1_1_2 == "1":        #accept again
            path1_1_2_1 = scene1_1_1()
            if path1_1_2_1 == "1":        #across mountains
                path1_1_2_1_1 = scene1_1_1_1()
                if path1_1_2_1_1 == "1":      #descend towards the fortress
                    path1_1_2_1_1_1 = scene1_1_1_1_1()
                    if path1_1_2_1_1_1 == "1":        #charge it down boldly
                        path1_1_2_1_1_1_1 = scene1_1_1_1_1_1()
                        if path1_1_2_1_1_1_1 == "1":      #defend with scraps
                            end(scene1_1_1_1_1_1_1())
                        elif path1_1_2_1_1_1_1 == "2":        #attack while charging
                            win(scene1_1_1_1_1_1_2())
                    elif path1_1_2_1_1_1 == "2":      #gather intel
                        win(scene1_1_1_1_1_2())
                elif path1_1_2_1_1 == "2":        #setup camp and observe
                    path1_1_2_1_1_2 = scene1_1_1_1_2()
                    if path1_1_2_1_1_2 == "1":        #hide behind rock
                        path1_1_2_1_1_2_1 = scene1_1_1_1_2_1()
                        if  path1_1_2_1_1_2_1 == "1":     #wait for landing
                             end(scene1_1_1_1_2_1_1())
                        elif path1_1_2_1_1_2_1 == "2":        #shoot crossbows
                            win(scene1_1_1_1_2_1_2())
                    elif path1_1_2_1_1_2 == "2":      #reload crossbows
                        end(scene1_1_1_1_2_2())
            elif path1_1_2_1 == "2":      #through forest
                path1_1_2_1_2 = scene1_1_1_2()
                if path1_1_2_1_2 == "1":      # pay them
                    path1_1_2_1_2_1 = scene1_1_1_2_1()
                    if path1_1_2_1_2_1 == "1":        #ascend to fort
                        path1_1_2_1_2_1_1 = scene1_1_1_2_1_1()
                        if path1_1_2_1_2_1_1 == "1":        #charge it down boldly
                            path1_1_2_1_2_1_1_1 = scene1_1_1_1_1_1()
                            if path1_1_2_1_2_1_1_1 == "1":      #defend with scraps
                                end(scene1_1_1_1_1_1_1())
                            elif path1_1_2_1_2_1_1_1 == "2":        #attack while charging
                                win(scene1_1_1_1_1_1_2())
                        elif path1_1_2_1_2_1_1 == "2":      #gather intel
                            win(scene1_1_1_1_1_2())
                    elif path1_1_2_1_2_1 == "2":      #head home
                        end(scene1_1_1_2_1_2())
                elif path1_1_2_1_2 == "2":    # talk it out
                    end(scene1_1_1_2_2())
                elif path1_1_2_1_2 == "3":    # unspeakable violence
                    path1_1_2_1_2_3 = scene1_1_1_2_3()
                    if path1_1_2_1_2_3 == "1":        # ascend
                        path1_1_2_1_2_3_1 = scene1_1_1_2_3_1()
                        if path1_1_2_1_2_3_1 == "1":        #charge it down boldly
                            path1_1_2_1_2_3_1_1 = scene1_1_1_1_1_1()
                            if path1_1_2_1_2_3_1_1 == "1":      #defend with scraps
                                end(scene1_1_1_1_1_1_1())
                            elif path1_1_2_1_2_3_1_1 == "2":        #attack while charging
                                win(scene1_1_1_1_1_1_2())
                        elif path1_1_2_1_2_3_1 == "2":     # head home
                            end(scene1_1_1_2_3_2())
        elif path1_1_2 == "2":      #decline again
            end(scene1_1_2_2())

elif path1 == "2":      #throw table
    path1_2 = scene1_2()
    if path1_2 == "1":      #help him up
        path1_2_1 = scene1_2_1()
        if path1_2_1 == "1":        #Accept
            path1_2_1_1 = scene1_2_1_1()
            if path1_2_1_1 == "1":      #kys
                end(scene1_2_1_1_1())
            elif path1_2_1_1 == "2":        #kill companion
                path1_2_1_1_2 = scene1_2_1_1_2()
                if path1_2_1_1_2 == "1":
                    end(scene1_2_1_1_2_1())
                elif path1_2_1_1_2 == "2":
                    win2(scene1_2_1_1_2_2())
            elif path1_2_1_1 == "3":        #sac stranger
                win2(scene1_2_1_1_3())
        elif path1_2_1 == "2":      #decline
            path1_2_1_2 = scene1_1_2()
            if path1_2_1_2 == "1":
                path1_2_1_2_1 = scene1_2_1_1()
                if path1_2_1_2_1 == "1":      #kys
                    end(scene1_2_1_1_1())
                elif path1_2_1_2_1 == "2":        #kill companion
                    path1_2_1_2_1_2 = scene1_2_1_1_2()
                    if path1_2_1_2_1_2 == "1":
                        end(scene1_2_1_1_2_1())
                    elif path1_2_1_2_1_2 == "2":
                        win2(scene1_2_1_1_2_2())
                elif path1_2_1_2_1 == "3":        #sac stranger
                    win2(scene1_2_1_1_3())
            elif path1_2_1_2 == "2":      #decline again
                end(scene1_1_2_2() )
    elif path1_2 == "2":      #kill him
        end(scene1_2_2())
    elif path1_2 == "3":        #wait
        end(scene1_2_3())

elif path1 == "3":      #do nothing
    path1_3 = scene1_3()
    if path1_3 == "1":      #accept
        path1_3_1 = scene1_1_1()
        if path1_3_1 == "1":        #across mountains
            path1_3_1_1 = scene1_1_1_1()
            if path1_3_1_1 == "1":      #descend towards the fortress
                path1_3_1_1_1 = scene1_1_1_1_1()
                if path1_3_1_1_1 == "1":        #charge it down boldly
                    path1_3_1_1_1_1 = scene1_1_1_1_1_1()
                    if path1_3_1_1_1_1 == "1":      #defend with scraps
                        end(scene1_1_1_1_1_1_1())
                    elif path1_3_1_1_1_1 == "2":        #attack while charging
                        win(scene1_1_1_1_1_1_2())
                elif path1_3_1_1_1 == "2":      #gather intel
                    win(scene1_1_1_1_1_2())
            elif path1_3_1_1 == "2":        #setup camp and observe
                path1_3_1_1_2 = scene1_1_1_1_2()
                if path1_3_1_1_2 == "1":        #hide behind rock
                    path1_3_1_1_2_1 = scene1_1_1_1_2_1()
                    if  path1_3_1_1_2_1 == "1":     #wait for landing
                         end(scene1_1_1_1_2_1_1())
                    elif path1_3_1_1_2_1 == "2":        #shoot crossbows
                        win(scene1_1_1_1_2_1_2())
                elif path1_3_1_1_2 == "2":      #reload crossbows
                    end(scene1_1_1_1_2_2())
        elif path1_3_1 == "2":      #through forest
            path1_3_1_2 = scene1_1_1_2()
            if path1_3_1_2 == "1":      # pay them
                path1_3_1_2_1 = scene1_1_1_2_1()
                if path1_3_1_2_1 == "1":        #ascend to fort
                    path1_3_1_2_1_1 = scene1_1_1_2_1_1()
                    if path1_3_1_2_1_1 == "1":        #charge it down boldly
                        path1_3_1_2_1_1_1 = scene1_1_1_1_1_1()
                        if path1_3_1_2_1_1_1 == "1":      #defend with scraps
                            end(scene1_1_1_1_1_1_1())
                        elif path1_3_1_2_1_1_1 == "2":        #attack while charging
                            win(scene1_1_1_1_1_1_2())
                    elif path1_3_1_2_1_1 == "2":      #gather intel
                        win(scene1_1_1_1_1_2())
                elif path1_3_1_2_1 == "2":      #head home
                    end(scene1_1_1_2_1_2())
            elif path1_3_1_2 == "2":    # talk it out
                end(scene1_1_1_2_2())
            elif path1_3_1_2 == "3":    # unspeakable violence
                path1_3_1_2_3 = scene1_1_1_2_3()
                if path1_3_1_2_3 == "1":        # ascend
                    path1_3_1_2_3_1 = scene1_1_1_2_3_1()
                    if path1_3_1_2_3_1 == "1":        #charge it down boldly
                        path1_3_1_2_3_1_1 = scene1_1_1_1_1_1()
                        if path1_3_1_2_3_1_1 == "1":      #defend with scraps
                            end(scene1_1_1_1_1_1_1())
                        elif path1_3_1_2_3_1_1 == "2":        #attack while charging
                            win(scene1_1_1_1_1_1_2())
                    elif path1_3_1_2_3 == "2":     # head home
                        end(scene1_1_1_2_3_2())
    elif path1_3 == "2":        #decline
        path1_3_2 = scene1_1_2()
        if path1_3_2 == "1":        #accept again
            path1_3_2_1 = scene1_1_1()
            if path1_3_2_1 == "1":        #across mountains
                path1_3_2_1_1 = scene1_1_1_1()
                if path1_3_2_1_1 == "1":      #descend towards the fortress
                    path1_3_2_1_1_1 = scene1_1_1_1_1()
                    if path1_3_2_1_1_1 == "1":        #charge it down boldly
                        path1_3_2_1_1_1_1 = scene1_1_1_1_1_1()
                        if path1_3_2_1_1_1_1 == "1":      #defend with scraps
                            end(scene1_1_1_1_1_1_1())
                        elif path1_3_2_1_1_1_1 == "2":        #attack while charging
                            win(scene1_1_1_1_1_1_2())
                    elif path1_3_2_1_1_1 == "2":      #gather intel
                        win(scene1_1_1_1_1_2())
                elif path1_3_2_1_1 == "2":        #setup camp and observe
                    path1_3_2_1_1_2 = scene1_1_1_1_2()
                    if path1_3_2_1_1_2 == "1":        #hide behind rock
                        path1_3_2_1_1_2_1 = scene1_1_1_1_2_1()
                        if  path1_3_2_1_1_2_1 == "1":     #wait for landing
                             end(scene1_1_1_1_2_1_1())
                        elif path1_3_2_1_1_2_1 == "2":        #shoot crossbows
                            win(scene1_1_1_1_2_1_2())
                    elif path1_3_2_1_1_2 == "2":      #reload crossbows
                        end(scene1_1_1_1_2_2())
            elif path1_3_2_1 == "2":      #through forest
                path1_3_2_1_2 = scene1_1_1_2()
                if path1_3_2_1_2 == "1":      # pay them
                    path1_3_2_1_2_1 = scene1_1_1_2_1()
                    if path1_3_2_1_2_1 == "1":        #ascend to fort
                        path1_3_2_1_2_1_1 = scene1_1_1_2_1_1()
                        if path1_3_2_1_2_1_1 == "1":        #charge it down boldly
                            path1_3_2_1_2_1_1_1 = scene1_1_1_1_1_1()
                            if path1_3_2_1_2_1_1_1 == "1":      #defend with scraps
                                end(scene1_1_1_1_1_1_1())
                            elif path1_3_2_1_2_1_1_1 == "2":        #attack while charging
                                win(scene1_1_1_1_1_1_2())
                        elif path1_3_2_1_2_1_1 == "2":      #gather intel
                            win(scene1_1_1_1_1_2())
                    elif path1_3_2_1_2_1 == "2":      #head home
                        end(scene1_1_1_2_1_2())
                elif path1_3_2_1_2 == "2":    # talk it out
                    end(scene1_1_1_2_2())
                elif path1_3_2_1_2 == "3":    # unspeakable violence
                    path1_3_2_1_2_3 = scene1_1_1_2_3()
                    if path1_3_2_1_2_3 == "1":        # ascend
                        path1_3_2_1_2_3_1 = scene1_1_1_2_3_1()
                        if path1_3_2_1_2_3_1 == "1":        #charge it down boldly
                            path1_3_2_1_2_3_1_1 = scene1_1_1_1_1_1()
                            if path1_3_2_1_2_3_1_1 == "1":      #defend with scraps
                                end(scene1_1_1_1_1_1_1())
                            elif path1_3_2_1_2_3_1_1 == "2":        #attack while charging
                                win(scene1_1_1_1_1_1_2())
                        elif path1_3_2_1_2_3_1 == "2":      #gather intel
                            win(scene1_1_1_1_1_2())
                    elif path1_3_2_1_2_3 == "2":     # head home
                        end(scene1_1_1_2_3_2())
        elif path1_3_2 == "2":      #decline again
            end(scene1_1_2_2())