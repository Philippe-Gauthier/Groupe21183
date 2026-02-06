#libraries
import time
import random

#game logic
debug_delay = 0

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
    print("(1) across the mountains, it may be perrilous but it's the fastest route")
    print("(2) around, by the forest, it may take longer but it's safer")
    path1_1_1 = input("Where to? (1/2): ")
    return path1_1_1

##scene 1_1_1_1, across mountains       open
def scene1_1_1_1():
    print_("1111")

##scene 1_1_1_2, around forest      open
def scene1_1_1_2():
    print_("1112")

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

##scene 1_1_2_1, accept     open
def scene1_1_2_1():
    print_("1121")

##scene 1_1_2_2, decline      open
def scene1_1_2_2():
    print_("1122")

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
    print("(3) Leave him there and walk away")
    path1_2 = input("What do you do? (1/2/3): ")
    return path1_2

##scene 1_2_1, help him up      open
def scene1_2_1():
    print_("121")

##scene 1_2_2, kill him     open
def scene1_2_2():
    print_("122")

##scene 1_2_3, walk away        open
def scene1_2_3():
    print_("123")


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

##scene 1_3_1, accept
def scene1_3_1():
    print_("\n\nYou accept, finaly, a quest worthy of your legendary skills.")
    print_(""""We shall leave at dawn", he says, "meet me at the town gates." """)
    print_("you part ways as to not attreact attention further and go to your cottage.")
    print_("as the sun creeps over the nearby hills you make your way to the town's edge where the man awaits with horses and provisions")
    print_(""""Onwards" you enthoustiacally call once all is set." """)
    print_(""""to which path?" he anwsers,"we should decide on the road." """)
    print_(""""quite right" you say, we shall pass... """)

    time.sleep(debug_delay * 2)
    print("\n--- where will you go? ---")
    print("(1) across the mountains, it may be perrilous but it's the fastest route")
    print("(2) around, by the forest, it may take longer but it's safer")
    path1_3_1 = input("Where to? (1/2): ")
    return path1_3_1

##scene 1_3_1_1, across mountains       open and clone
def scene1_3_1_1():
    print_("1311")

##scene 1_3_1_2, around forest      open and clone
def scene1_3_1_2():
    print_("1312")

##scene 1_3_2, decline
def scene1_3_2():
    print_("\n\nYou politely decline the offer, although you may be a great adventurer, an ice wyrm is not to be trifled with.")
    print_(""""That is why I require a companion" he says,"I cannot do this alone and neither can you, but together..." """)
    print_("it is true that you have no idea of the man's skills, it may be possible and even likely that he is as capable as you are.")
    print_("the idea starts to tempt you, you imagine the glory and riches that would come from slaying such a beast.")

    time.sleep(debug_delay * 2)
    print("\n--- Do you change your mind? ---")
    print("(1) Accept")
    print("(2) Decline")
    path1_3_2 = input("What do you do? (1/2): ")
    return path1_3_2

##scene 1_3_2_1, accept     open and clone
def scene1_3_2_1():
    print_("1321")

##scene 1_3_2_2, decline      open and clone
def scene1_3_2_2():
    print_("1322")


#gameplay tree

name = intro()
path1 = scene1()
if path1 == "1":
    path1_1 = scene1_1()
    if path1_1 == "1":
        path1_1_1 = scene1_1_1()
        if path1_1_1 == "1":
            scene1_1_1_1()
        elif path1_1_1 == "2":
            scene1_1_1_2()
    elif path1_1 == "2":
        path1_1_2 = scene1_1_2()
        if path1_1_2 == "1":
            scene1_1_2_1()
        elif path1_1_2 == "2":
            scene1_1_2_2()

elif path1 == "2":
    path1_2 = scene1_2()
    if path1_2 == "1":
        scene1_2_1()
    elif path1_2 == "2":
        scene1_2_2()
    elif path1_2 == "3":
        scene1_2_3()

elif path1 == "3":
    path1_3 = scene1_3()
    if path1_3 == "1":
        path1_3_1 = scene1_3_1()
        if path1_3_1 == "1":
            scene1_3_1_1()
        elif path1_3_1 == "2":
            scene1_3_1_2()
    elif path1_3 == "2":
        path1_3_2 = scene1_3_2()
        if path1_3_2 == "1":
            scene1_3_2_1()
        elif path1_3_2 == "2":
            scene1_3_2_2()