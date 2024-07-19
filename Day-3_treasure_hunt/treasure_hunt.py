print(
    """ _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_| 
"""
)

print("The Treasure of Mystic Isle".center(80))
print(
    """
On a remote and mysterious island, known to sailors as Mystic Isle, there lies a hidden treasure, long sought after by adventurers and pirates alike.\n This island, surrounded by treacherous waters and guarded by fierce storms, has remained largely unexplored. Only the bravest dare to step foot on its shores.\n
Our story begins with you, an intrepid adventurer, washing up on the sandy beach of Mystic Isle after your ship was wrecked in a violent storm. As you regain your senses, you notice a tattered map clutched in your hand—a map that promises unimaginable riches hidden deep within the island's heart.
"""
)

print(
    """
With the sun setting behind the jagged cliffs, you decide to set off immediately. The journey starts at the beach, where you find an old wooden signpost with two \n directions: "Dense Jungle" and "Rocky Path". Each path holds its own dangers and secrets.
"""
)

first_destination = input(
    "Which direction do you choose? Dense Jungle or Rocky Path "
).lower()
if first_destination == "dense jungle":
    print(
        """
    You choose to venture through the dense jungle, where the air is thick with humidity and the sounds of unknown creatures echo around you. As you make your way through the jungle, you stumble upon a clearing with an ancient stone statue. At its base, a cryptic riddle is inscribed:\n
    "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?"
    """
    )

    first_riddle = input("Enter the answer: ").lower().strip()
    if first_riddle == "echo":
        print(
            "Right answer! The statue's eyes glow momentarily, revealing a hidden passageway beneath it."
        )

        print(
            """
        Crawling through the narrow passage, you find yourself in a cavern lit by bioluminescent fungi. At the center of the cavern lies a crystal-clear pond, its waters reflecting a beautiful but deadly creature—a guardian serpent.\n The serpent speaks,
        "Answer my question to pass: What walks on four legs in the morning, two legs at noon, and three legs in the evening?"
        """
        )

        second_riddle = input("Enter the answer: ").lower().strip()
        if second_riddle == "man":
            print(
                "Correct! The serpent nods and sinks back into the depths, allowing you to cross the pond."
            )

            print(
                """
            Emerging from the cavern, you stand at the entrance of an ancient temple. Inside, the final challenge awaits. The temple's grand hall is filled with an \n intricate pattern of tiles, each marked with different symbols. You recall the map's clue: "The path of the sun will guide you."
            Carefully, you step on the tiles in the order of the sun's journey across the sky—from sunrise to sunset. As you complete the pattern, the temple walls begin \n to tremble, revealing a hidden chamber.       
            In the chamber, a magnificent treasure chest rests on a pedestal, surrounded by glittering gold coins, jewels, and artifacts of untold value. Your heart races with excitement as you open the chest, discovering not only the wealth but also a mysterious artifact—an ancient amulet said to possess the power to control the \n island's weather.
            With the treasure secured and the amulet in your possession, you make your way back to the beach. The storm that brought you here has cleared, and the calm sea invites \n you to set sail once more. As you leave Mystic Isle, you carry with you not only the riches but also the stories and secrets of the island, ready to share \n with those who dare to dream of adventure.
            And so, the legend of the treasure of Mystic Isle continues, awaiting the next brave soul to uncover its mysteries.
            """
            )
        else:
            print(
                "Wrong answer. The guardian serpent strikes, and your adventure ends here."
            )
    else:
        print(
            "Wrong answer. The statue remains silent and unyielding, and your adventure ends here."
        )
else:
    print(
        "You chose the Rocky Path. The path is steep and treacherous, but you continue on your journey."
    )
