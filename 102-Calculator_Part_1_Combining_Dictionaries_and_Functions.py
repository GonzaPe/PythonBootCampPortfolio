#from art import logo
xyrg = "hello "
print(type(x))
#print(logo)

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


num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))
for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")

function = operations[operation_symbol]
result = function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {result}")