from art import logo
import os

print(logo)

is_bid_done = False
bids = []

while not is_bid_done:
    while True:
        bidder_name = input("Enter your name: ").strip()
        if bidder_name.isalpha():
            break
        else:
            print("Name must contain only letters. Please enter a valid name.")

    while True:
        try:
            price = int(input("Enter the bid price: $"))
            if price > 0:
                break
            else:
                print("Bid price must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for the bid price.")

    while True:
        next_person = input("Any other wants to bid? (yes/no): ").strip().lower()
        if next_person in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Storing the bids
    bids.append({"name": bidder_name, "price": price})

    if next_person == "yes":
        os.system("cls" if os.name == "nt" else "clear")
    elif next_person == "no":
        is_bid_done = True


def auction_bid(bids):
    # Initialize the highest bid
    highest_bid = bids[0]

    # Iterate through the bids to find the highest
    for bid in bids:
        if bid["price"] > highest_bid["price"]:
            highest_bid = bid

    print(
        f"The highest bid is by {highest_bid['name']} with a bid of ${highest_bid['price']}"
    )


auction_bid(bids)
