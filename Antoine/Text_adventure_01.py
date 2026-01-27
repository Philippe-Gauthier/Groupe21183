#libraries
import time

#game logic
def print_ (text, delay=0.5):
    print(text)
    time.sleep(delay)

#scenes

##scene 1, starting point
def scene1():
    print_("Welcome to the Text Adventure Game!")
    name = input("What is your name, adventurer? ")
    print_(f"Hello, {name}! Your journey begins now.")
    print_("You wake up from a deep slumber at a corner table in your local taverne.")
    print_("As you steadily regain consciousness, you notice a hooded figure sitting across from you.")
    print_("Just as you noticed it, it noticed you and is now rapidly approaching your table in strong, heavy strides.")
    

    print("\n--- What do you do? ---")
    print("option1")
    print("option2")
    print("option3")
    path1 = input("choice: ")
    return path1

#gameplay tree
print(scene1())
path1 = scene1()
if path1 == "1":
    print_("choice1")
elif path1 == "2":
    print_("choice2")  
elif path1 == "3":
    print_("choice3")