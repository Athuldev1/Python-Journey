from caesar_art import logo, alphabet

print(logo)


def caesar_cipher(start_text, shift_amount, cipher_direction):
    final_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    elif cipher_direction != "encode":
        raise ValueError("Invalid direction. Use 'encode' or 'decode'.")

    alphabet_length = len(alphabet)
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % alphabet_length
            final_text += alphabet[new_position]
        else:
            final_text += char
    print(f"The {cipher_direction}d text is {final_text}.")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ["encode", "decode"]:
        print("Invalid input. Please type 'encode' or 'decode'.")
        continue

    text = input("Type your message:\n").lower()
    try:
        shift = int(input("Type the shift number:\n"))
    except ValueError:
        print("Invalid shift number. Please enter an integer.")
        continue
    shift %= len(alphabet)
    caesar_cipher(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input(
        "Type 'yes' if you want to restart or 'no' if you want to exit the program: "
    ).lower()
    if result == "no":
        should_continue = False
        print("Goodbye!")
    elif result != "yes":
        print("ERROR! Please input 'yes' or 'no'!")
        should_continue = False
