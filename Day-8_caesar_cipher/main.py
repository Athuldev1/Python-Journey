from caesar_art import logo, alphabet

print(logo)


def caesar(start_text, shift_amount, cipher_direction):
    final_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    else:
        print("Value error")

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % len(alphabet)
            final_text += alphabet[new_position]
        else:
            final_text += char
    print(f"The {cipher_direction}d text is {final_text}.")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # The program continues to work even if the user enters a shift number greater than 26
    shift %= len(alphabet)
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input(
        "Type 'yes' if you want to restart or 'no' if you want to exit the program: "
    ).lower()
    if result == "no":
        should_continue = False
        print("Goodbye!")
    elif result != "yes":
        print("ERROR! Please input 'yes' or 'no'!")
        should_continue = False
