# Inventory Management System

This is a simple command-line based Inventory Management System written in Python. The system allows users to manage an inventory of items by adding, updating, removing, and viewing items and their quantities.

## Features

- **Add Items**: Add new items to the inventory with a specified quantity.
- **Remove Items**: Remove items from the inventory.
- **Update Item Quantity**: Update the quantity of an existing item.
- **View Inventory**: View the current inventory along with the total number of items and quantities in stock.

## How to Use

1. **Add an Item**:  
   Select option `1` to add a new item. Enter the item name and quantity. The item will be added to the inventory.

2. **Remove an Item**:  
   Select option `2` to remove an item. Enter the item name to remove it from the inventory.

3. **Update Item Quantity**:  
   Select option `3` to update the quantity of an existing item. Enter the item name and the new quantity.

4. **View Inventory**:  
   Select option `4` to view the entire inventory along with item quantities, total number of items, and the total stock count.

5. **Exit**:  
   Select option `5` to exit the system.

## Example

Here's how a typical interaction looks like:

```plaintext
===== Welcome to the Inventory Management System =====
1. Add an item
2. Remove an item
3. Update item quantity
4. View inventory
5. Exit

Enter your choice: 1
Enter the item: apples
Enter the quantity: 10
Apples added successfully!

===== Welcome to the Inventory Management System =====
1. Add an item
2. Remove an item
3. Update item quantity
4. View inventory
5. Exit

Enter your choice: 4

Current Inventory:
Apples: 10

Total different items: 1
Total quantity in stock: 10
