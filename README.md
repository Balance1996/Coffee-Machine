Coffee Machine Project

Overview

This project simulates a coffee machine that allows users to select drinks, insert coins, check available resources, and refill the machine. It demonstrates the use of Python dictionaries, lists, loops, conditional statements, and functions to manage data and process transactions.

The project includes two refill variants: unlimited refills and limited refills.

Data Structures

Dictionaries are used to store related key-value pairs. Some basic examples include current_resources, coin, and refill_resources, which store the available ingredients, accepted coin denominations and values, and refill quantities.

The menu variable is a list of dictionaries. Each dictionary represents a drink and contains its name, required ingredients, and price. This structure makes it possible to retrieve information about a selected drink and update the machine's resources.

Dictionary methods such as .items() allow the program to iterate over key-value pairs. For example, loops can access ingredient names and quantities when displaying resource information or refilling the machine.

Functions and Their Responsibilities

status_report()

Displays the machine's current resources and accepted coin denominations with their corresponding values. It uses dictionary iteration to present the information in a readable format.

get_price(user_choice)

Iterates through the dictionaries in menu to find the drink matching user_choice. If a match is found, the function returns the drink's price. Otherwise, it returns None, allowing the program to recognize an invalid drink selection.

cal_price(penny_input, nickel_input, dime_input, quarter_input, user_choice)

Calculates the total value of the inserted coins using the number of coins entered and their respective denominations. It then subtracts the selected drink's price and returns the resulting change, rounded to two decimal places. If the drink is invalid, the function returns None.

refill_machine()

Updates current_resources by adding the quantities specified in refill_resources. This function centralizes the resource-refilling operation.

eval_price(user_choice, user_coins)

Processes a drink transaction by checking whether the selected drink exists, whether sufficient ingredients are available, and whether the payment covers the drink's price.

If any check fails, the function displays an appropriate message and avoids deducting ingredients. If all checks pass, it calculates the change, deducts the required ingredients, and confirms that the drink has been dispensed.

main()

Controls the main program loop and handles user input. It directs the program to the appropriate functions based on the user's selection, including ordering drinks, displaying a report, refilling resources, and shutting down the machine.

Key Concepts Practised

Working with dictionaries and lists of dictionaries.

Accessing and updating key-value pairs.

Using loops to search for matching data.

Separating program responsibilities into functions.

Validating user input and handling invalid selections.

Using conditional statements to control transaction flow.

Managing shared state, including resources and refill limits.

Calculating payments and change.

Future Improvements

Potential improvements include automated tests for successful and unsuccessful transactions, stronger input validation, and further refinement of the refill-limit mechanism.
