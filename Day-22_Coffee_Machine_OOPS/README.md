Coffee Machine Project

This project is an OOP-based simulation of a coffee machine, built using Python. The coffee machine can prepare different types of drinks (Espresso, Latte, Cappuccino) based on the resources available, and it handles user input to simulate a real coffee machine experience.

Features

Drinks Available: Espresso, Latte, Cappuccino
Resource Management: Keeps track of the resources like water, milk, coffee, and money.
User Input: Accepts user input for selecting drinks and inserting coins.
Coin Calculation: Calculates the total value of coins inserted by the user.
Object-Oriented Design: Utilizes classes to encapsulate machine behavior and functionality.

Class Structure
CoffeeMachine: The main class that manages the coffee machine's resources, checks availability, processes transactions, and makes drinks.
Drink: Represents a coffee drink with specific requirements (water, milk, coffee).
MoneyHandler: Handles the insertion of coins and calculation of total values.

How It Works
Initialization: A CoffeeMachine object is initialized with a set amount of water, milk, coffee, and money.
Different Drink objects are initialized with their specific resource requirements.
User Interaction: The machine prompts the user to choose a drink or view the report of available resources.
If a drink is selected, the machine checks for sufficient resources.
The user is then asked to insert coins, and the total value is calculated.
Transaction Processing: The machine compares the inserted coins' total value with the drink's cost.
If sufficient funds are provided, the drink is dispensed, resources are updated, and change is returned if necessary.
