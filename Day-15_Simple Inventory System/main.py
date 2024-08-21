inventory_system = {}


def add_items():
    add_item = input("Enter the item: ").lower()
    try:
        quantity = int(input("Enter the quantity: "))
        if quantity < 0:
            print("Quantity cannot be negative.")
            return
    except ValueError:
        print("Please enter a valid number for quantity.")
        return
    inventory_system[add_item] = quantity
    print(f"{add_item.capitalize()} added successfully!")


def remove_items():
    if not inventory_system:
        print("Inventory is empty. Nothing to remove.")
        return

    remove_item = input("Enter the item name to remove: ").lower()
    if remove_item in inventory_system:
        confirm = input(f"Are you sure you want to delete {remove_item}? (y/n): ").lower()
        if confirm == 'y':
            del inventory_system[remove_item]
            print(f"{remove_item.capitalize()} deleted successfully!")
        else:
            print("Deletion canceled.")
    else:
        print(f"{remove_item.capitalize()} is not in the system.")


def update_item_quantity():
    if not inventory_system:
        print("Inventory is empty. Nothing to update.")
        return

    update_item = input("Enter the item: ").lower()
    if update_item in inventory_system:
        try:
            update_quantity = int(input("Enter the quantity: "))
            if update_quantity < 0:
                print("Quantity cannot be negative.")
                return
        except ValueError:
            print("Please enter a valid number for quantity.")
            return
        inventory_system[update_item] = update_quantity
        print(f"{update_item.capitalize()} quantity updated successfully!")
    else:
        print(f"{update_item.capitalize()} is not in the system.")


def view_inventory():
    if inventory_system:
        print("\nCurrent Inventory:")
        for item, quantity in inventory_system.items():
            print(f"{item.capitalize()}: {quantity}")
        total_items = len(inventory_system)
        total_quantity = sum(inventory_system.values())
        print(f"\nTotal different items: {total_items}")
        print(f"Total quantity in stock: {total_quantity}")
    else:
        print("Inventory is empty. Start adding items!")


def main_menu():
    while True:
        print("\n===== Welcome to the Inventory Management System =====")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. Update item quantity")
        print("4. View inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_items()
        elif choice == "2":
            remove_items()
        elif choice == "3":
            update_item_quantity()
        elif choice == "4":
            view_inventory()
        elif choice == "5":
            print("Exiting the system...")
            break
        else:
            print("Invalid choice! Please select a valid option.")


def main():
    main_menu()


if __name__ == "__main__":
    main()
