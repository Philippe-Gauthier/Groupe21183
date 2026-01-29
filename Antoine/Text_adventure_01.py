#libraries
import time

#game logic
debug_delay = 0.5

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

    print_("\nYou wake up from a deep slumber at a corner table in your local taverne.")
    print_("As you steadily regain consciousness, you notice a hooded figure sitting across from you.")
    print_("Just as you noticed it, it noticed you and is now rapidly approaching your table in strong, heavy strides.")
    print_("Suddently, with a rush of adrenaline, you recall what it is you went to do here today,")
    print_("It wasn't simply to get drunk, although that is an always pleasant side effewct of meetings in pubs.")
    print_("Today was thge day where you would finally learn who sent that letter and why it was so vague.") #if an inventory system ever gets added, here would be th point to put a "mysterious letter added to inventory" line
    print_("""Indeed, last week, you were invited to be here, at this moment, for an "opportunity". """)
    print_("The hooded stranger sits down facing you and, without warning, unsheaths a dagger, propelling it's edge towards your throat")

    time.sleep(debug_delay * 2)
    print("\n--- What do you do? ---")
    print("(1) Lean back with your entire body do try and avoid the blade")
    print("(2) Throw the table upwards to deflect the blow")
    print("(3) Nothing")
    path1 = input("What do you do? (1/2/3): ")
    return path1

##scene 2, lean back
def scene1_1():
    print_("\n\nYou lean back with your entire body do try and avoid the blade")
    print_("It misses you by mere inches, then, just as swiftly as it had slashed, it retracted into it's sheath.")
    print_("It all happened so fast that, for al else present, it looked only as if you had fallen to the ground from alcohol, nothing more.")
    print_("The figure stands up and offers to help you back to your feet.")

##scene 2, throw table
def scene1_2():
    print_("\n\nYou rapidly raise your knees, lunching the table upwards with all your strength.")
    print_("The blade narrowly misses your chin, your legs it hurts and you're not one to leave pain unpunished.")
    print_("Taking advantage of the ensuing cahos, you spring over the tavern table, now split in two by the impact with your assailant's arms.")
    print_("Pushing him to the rough floor, punching him bloody, you pull out your own dagger and place it on his throat.")
    print_("Shouting over his struggles, you demand to know who he is and why he attacked you.")
    print_("After a long pause, the hooded figure speaks up, his voice hoarse and weak from the beating.")
    print_(""""please... not here... not now... must..." he gasps.""")
    
    time.sleep(debug_delay * 2)
    print("\n--- What do you do? ---")
    print("(1) Slowly help him up and order mead as an appology")
    print("(2) Let violence and adrenalline blind you and kill him")
    print("(3) L:eave him there and walk away")
    path2 = input("What do you do? (1/2/3): ")
    return path2

##scene 3, do nothing
def scene1_3():
    print_("\n\nYou stand your ground, facing down death in its eyes, stoic and unflinching.")
    print_("The hooded figure stops, centimeters from your throat with a slight chuckle, it sheaths its blade and lowers its hood.")
    print_(f""""You are {name},are you not? it says.""")
    print_("You aprehenctively nod, on your guard, hand on your dagger.")
    print_(""""You are indeed as brave and insightful as described, my time is not being wasted here". he continues.""")



#gameplay tree

name = intro()
path1 = scene1()
if path1 == "1":
    print_(scene1_1())
elif path1 == "2":
    print_(scene1_2())  
elif path1 == "3":
    print_(scene1_3())