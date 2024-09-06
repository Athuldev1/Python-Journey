Coffee Machine Project

This project simulates a simple coffee machine using Python. The coffee machine offers three types of drinks: Espresso, Latte, and Cappuccino. It manages resources, takes user input for coins, and calculates the total value of the coins to determine if a drink can be dispensed.

Features

Available Drinks: Espresso, Latte, Cappuccino
Resource Management: Tracks the availability of water, milk, coffee, and money.
User Input: Accepts input for the type of drink and the number of coins inserted.
Transaction Handling: Calculates the total amount of money inserted, checks if it is sufficient for the selected drink, and returns change if applicable.
Error Handling: Informs the user if there are insufficient resources or if the coins inserted are not enough for the selected drink.

How to Use

Run the Program: Start the program by executing the Python script.
Select a Drink: When prompted, enter the name of the drink (espresso, latte, or cappuccino) you would like to order. You can also type report to see the current status of resources or off to turn off the machine.
Insert Coins: If a drink is selected, you will be prompted to insert coins (quarters, dimes, nickels, pennies). Enter the number of each type of coin.
Receive Drink and Change: If enough money is provided, you will receive your drink and any change due.
Code Overview
resources Dictionary: Maintains the current levels of water, milk, coffee, and money in the machine.
drink_requirements Dictionary: Specifies the amount of each resource required for each type of drink.
drink_costs Dictionary: Defines the cost of each drink.
report() Function: Displays the current levels of resources.
check_resources(drink) Function: Checks if there are enough resources to make the selected drink.
calculate_coin_value(quarter, dime, nickel, penny) Function: Calculates the total value of inserted coins.
get_coin_input() Function: Accepts user input for the number of coins.
