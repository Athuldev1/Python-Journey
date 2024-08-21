# Room details stored in a dictionary
rooms = {
    "entrance": {
        "description": "You enter the dungeon and find yourself in a dimly lit hallway with two doors.",
        "actions": ["left", "right"]
    },
    "left_room": {
        "description": "You step into a room filled with ancient artifacts. In the corner, you see a shiny key.",
        "item": "shiny key"
    },
    "right_room": {
        "description": "You enter a room with a locked treasure chest. There’s nothing else to do here."
    },
    "downstairs": {
        "description": "You descend into a dark chamber. A fierce dragon stands before you!"
    }
}

def get_valid_input(prompt, options):
    """Handles input validation by accepting only the expected options."""
    while True:
        choice = input(prompt).lower().strip()
        if choice in options:
            return choice
        print("Invalid option. Please try again.")

def pickup_key():
    print("You now have the shiny key! It might be useful later.")
    return True  # Returns a value indicating the key was picked up

def downstairs(has_key):
    print(rooms["downstairs"]["description"])
    action = get_valid_input("What do you do? (fight / run / use key): ", ["fight", "run", "use key"])
    if action == "fight":
        print("You engage the dragon in battle, but it’s a tough fight. You lose.")
    elif action == "run":
        print("You attempt to flee, but the dragon catches up. It's dangerous here!")
    elif action == "use key":
        if has_key:
            print("You hold up the shiny key. The dragon steps back and reveals a hidden exit.\nYou escape and win!")
        else:
            print("You don’t have the key! The dragon isn’t impressed.")

def open_another_door(has_key):
    print("The door creaks open, revealing a staircase leading downward.")
    action = get_valid_input("Do you want to go down the stairs or return to the hallway? (downstairs / return): ", ["downstairs", "return"])
    if action == "downstairs":
        downstairs(has_key)
    elif action == "return":
        print("You go back to the hallway and explore other options.")

def left_door():
    print(rooms["left_room"]["description"])
    action = get_valid_input("What do you want to do? (pick up key / leave): ", ["pick up key", "leave"])
    has_key = False
    if action == "pick up key":
        has_key = pickup_key()
        another_door = get_valid_input("There is another door in the room. Do you want to open it? (yes / no): ", ["yes", "no"])
        if another_door == "yes":
            open_another_door(has_key)
        else:
            print("You decide to leave the room.")
    else:
        print("You leave the room without taking the key, possibly making it harder to progress.")
    return has_key

def enter_the_room():
    print(rooms["entrance"]["description"])
    has_key = False
    direction = get_valid_input("Do you want to go left or right? (left / right): ", ["left", "right"])
    if direction == "left":
        has_key = left_door()
    elif direction == "right":
        print(rooms["right_room"]["description"])
    return has_key

def dungeon():
    print("Welcome, adventurer! You find yourself at the entrance of a dark and mysterious dungeon.")
    door = get_valid_input("Would you like to enter? (yes / no): ", ["yes", "no"])
    if door == "yes":
        has_key = enter_the_room()
        print("You return to the hallway with your next adventure ahead.")
    else:
        print("Exiting...")

def main():
    dungeon()

if __name__ == "__main__":
    main()
