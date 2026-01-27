import time
#print text with delay, for esthetics and ambiance
def print_with_delay(text, delay=0.5):
    print(text)
    time.sleep(delay)

#scene1 - tavern encounter
def scene1(name):
    print_with_delay("You wake up from a deep slumber at a corner table in your local taverne.")
    print_with_delay("As you steadily regain consciousness, you notice a hooded figure sitting across from you.")
    print_with_delay("Just as you noticed it, it noticed you and is now rapidly approaching your table in strong, heavy strides.")
    
    print("\n--- What do you do? ---")
    print("1. Stand up and confront the figure")
    print("2. Try to escape through the back door")
    print("3. Call for the tavern keeper")
    
    choice = input("\nEnter your choice (1-3): ")
    return choice

#Scene1-1: Confronting the hooded figure
def scene2_confront(name):
    print_with_delay("\nYou stand up bravely, meeting the figure face to face.")
    print_with_delay("The figure pulls back their hood, revealing an old friend!")
    print_with_delay(f"'{name}! I've been looking everywhere for you!'")
    # Add more to scenes here

#Scene1-2: Attempting escape
def scene2_escape(name):
    print_with_delay("\nYou quickly move toward the back door...")
    print_with_delay("You make it outside into the alley!")
    # Add more to scenes here

#Scene1-3: Calling for help
def scene2_tavern_keeper(name):
    print_with_delay("\nYou wave frantically at the tavern keeper.")
    print_with_delay("The figure stops in their tracks...")
    # Add more to scenes here

def main():
    print("Welcome to the Text Adventure Game!")
    name = input("What is your name, adventurer? ")
    print(f"Hello, {name}! Your journey begins now.")
    time.sleep(0.5)
    
    # Start the game
    choice = scene1(name)
    
    if choice == "1":
        scene2_confront(name)
    elif choice == "2":
        scene2_escape(name)
    elif choice == "3":
        scene2_tavern_keeper(name)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()