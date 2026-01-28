#libraries
import time

#game logic
debug_delay = 0.5

def print_ (text, delay=debug_delay):
    print(text)
    time.sleep(delay)

#scenes

##scene 1, starting point
def scene1():
    print_("\n\nWelcome to the Text Adventure Game!")
    name = input("What is your name, adventurer? ")
    print_(f"Hello, {name}! Your journey begins now.")
    print_("\nYou wake up from a deep slumber at a corner table in your local taverne.")
    print_("As you steadily regain consciousness, you notice a hooded figure sitting across from you.")
    print_("Just as you noticed it, it noticed you and is now rapidly approaching your table in strong, heavy strides.")
    print_("suddently, with a rush of adrenaline, you recall what it is you went to do here today,")
    print_("it wasn't simply to get drunk, although that is an always pleasant side effewct of meetings in pubs.")
    print_("Today was thge day where you would finally learn who sent that letter and why it was so vague.") #if an inventory system ever gets added, here would be th point to put a "mysterious letter added to inventory" line
    print_("""Indeed, last week, you were invited to be here, at this moment, for an "opportunity". """)
    print_("The hooded stranger sits down facing you and, without warning, unsheaths a dagger, propelling it's edge towards your throat")

    time.sleep(debug_delay+0.5)
    print("\n--- What do you do? ---")
    print("(1) lean back with your entire body do try and avoid the blade")
    print("(2) throw the table upwards to deflect the blow")
    print("(3) nothing")
    path1 = input("What do you do? (1/2/3): ")
    return path1

##scene 2, lean back
def scene1_1():
    print_("\n\nyou lean back with your entire body do try and avoid the blade")
    print_("it misses you by mere inches, then, just as swiftly as it had slashed, it retracted into it's sheath.")
    print_("it all happened so fast that, for al else present, it looked only as if you had fallen to the ground from alcohol, nothing more.")

##scene 2, throw table
def scene1_2():
    print_("choice2")

##scene 3, do nothing
def scene1_3():
    print_("\n\nyou stand your ground, facing down death in its eyes, stoic and unflinching.")
    print_("the hooded figure stops, with a slight chuckle, it sheaths its blade and lowers its hood.")
    print_(""" "you are indeed as brave and insightful as described, my time is not being wasted here" , it says.""")

#gameplay tree

path1 = scene1()
if path1 == "1":
    print_(scene1_1())
elif path1 == "2":
    print_(scene1_2())  
elif path1 == "3":
    print_(scene1_3())