def coffee_machine pseudocode():
    return print("""
CREATE a menu containing:
    Espresso: required resources and price
    Latte: required resources and price
    Cappuccino: required resources and price

CREATE a dictionary of coin values

CREATE a dictionary of current resources

IMPORT time module for a short processing delay

xxxxxx
FUNCTION get_report:
    DISPLAY a heading

    FOR each ingredient and amount in current resources:
        DISPLAY the ingredient and its amount
yyyyyy
FUNCTION get_price(user_choice):
    FOR each drink in the menu:
        IF the drink's name matches the user's choice:
            RETURN the drink's price

    RETURN None because no matching drink was found
zzzzz
FUNCTION cal_coins(number of pennies, nickels, dimes, quarters):
    CALCULATE total payment:
        pennies × penny value
        PLUS nickels × nickel value
        PLUS dimes × dime value
        PLUS quarters × quarter value

    ROUND the total to 2 decimal places

    RETURN the total payment
^^^^^
FUNCTION cal_price(user_sum, user_choice):
    GET the drink's price using get_price

    IF the drink has no price:
        RETURN None

    CALCULATE payment minus drink price

    ROUND the result to 2 decimal places

    RETURN the change
$$$$$
FUNCTION eval_price(user_sum, user_choice, current_resources, menu):

    SET selected_drink to None

    FOR each drink in the menu:
        IF the drink's name matches the user's choice:
            SET selected_drink to that drink
            STOP searching

    IF selected_drink is None:
        DISPLAY that the drink is unavailable
        EXPLAIN that payment must be refunded if applicable
        EXIT the function

    GET the selected drink's price

    FOR each ingredient and required amount in the selected drink:
        IF available amount is less than required amount:
            DISPLAY which ingredient is insufficient
            EXPLAIN that payment must be refunded if applicable
            EXIT the function

    IF payment is less than the drink's price:
        DISPLAY insufficient payment
        EXPLAIN that payment must be refunded
        EXIT the function

    CALCULATE the change

    DISPLAY payment received
    DISPLAY drink price
    DISPLAY change
    DISPLAY the successful purchase message

    FOR each ingredient and required amount in the selected drink:
        SUBTRACT the required amount from current resources
Main()
FUNCTION main:

    REPEAT indefinitely:

        DISPLAY machine instructions

        ASK the user to enter a drink, report, or off command
        CONVERT the input to lowercase and remove surrounding spaces

        IF the user enters "off":
            DISPLAY shutdown message
            EXIT the loop

        ELSE IF the user enters "report":
            CALL get_report
            SKIP the remaining steps and start the next loop iteration

        IF get_price(user_choice) returns None:
            DISPLAY that the drink is unavailable
            START the next loop iteration

        DISPLAY resource-checking message
        WAIT briefly

        TRY:
            ASK for the number of each coin

            IF any coin count is negative:
                DISPLAY an error
                START the next loop iteration

        IF converting an input to an integer fails:
            DISPLAY an input error
            START the next loop iteration

        CALCULATE total payment using cal_coins

        DISPLAY transaction-processing message

        CALL eval_price with:
            total payment
            user's drink choice
            current resources
            menu

WHEN the program is run directly:
    CALL main
""")