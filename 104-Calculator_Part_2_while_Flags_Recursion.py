#from art import logo
#print(logo)

from operator import truediv

def add(n1, n2):
    """Función para sumar (número 1, número 2)"""
    return n1+n2

def substract(n1, n2):
    """Función para restar (número 1, número 2)"""
    return n1-n2

def multiply(n1, n2):
    """Función para multiplicar (número 1, número 2)"""
    return n1*n2

def divide(n1, n2):
    """Función para dividir (número 1, número 2)"""
    return n1/n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = int(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What's the second number? "))

    function = operations[operation_symbol]

    result = function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")

    should_continue = True

    while should_continue == True:
        lets_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit: ")
        if lets_continue == "y":
            old_result = result
            for symbol in operations:
                print(symbol)
            operation_symbol = input("Pick an operation from the line above: ")
            num2 = int(input("What's the next number? "))
            function = operations[operation_symbol]
            result = function(old_result, num2)
            print(f"{old_result} {operation_symbol} {num2} = {result}")
        elif lets_continue == "n":
            should_continue = False
            print("Thank you for use this calculator. Have a nice day!")
            calculator()
        else:
            print("Please, type a 'y' or 'n'.")

calculator()