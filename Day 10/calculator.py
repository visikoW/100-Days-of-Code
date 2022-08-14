"""Program to calculate all numbers, including the decimal.
For example: Add, Subtract, Multiply and Divide."""

# Add
def add(n1: int, n2: int):
    """Add a number to the current number e.g. add(1, 2) will return 3."""
    return n1 + n2

# Subtract
def subtract(n1: int, n2: int):
    """Subtract a number from the current number e.g. subtract(1, 2) will return -1."""
    return n1 - n2

# Multiply
def multiply(n1: int, n2: int):
    """Multiply a number from the current number e.g. multiply(1, 2) will return 2."""
    return n1 * n2

# Divide
def divide(n1: int, n2: int):
    """Divide a number from the current number e.g. divide(1, 2) will return 0.5."""
    return n1 / n2

def search_operations():
    """Return all operations"""
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
    return operations

# Print all operators
def show_operations():
    """Show all operators on screen"""
    operations = search_operations()
    for x in operations:
        print(x)

def calculate(num1, num2):
    """Calculate 2 numbers"""
    operations = search_operations()

    # First: Choose one of those operators "+", "-", "*" or "/"
    show_operations()
    operation_symbol = input("Pick an operation: ")

    # Second: Calculate the num1, and num2 to get the result and return
    result_function = operations[operation_symbol]
    result = result_function(num1, num2)

    return result

def answer():
    """Calculate all operations and return the calculation"""
    # First: Ask to user to insert 2 number, the first and second
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))

    # Second: Save the result
    result = calculate(num1, num2)

    # Third: If the user want to insert another number, the answer must be "y" ou anything instead "n"
    while True :
        # First: Ask to continue
        test = input(f"Type 'y' to continue calculating with {result}, or 'n' to exit.: ")
        if test == "n":
            break

        # Second if First pass: save the last_answer to increment the nex number
        last_answer = result
        num3 = int(input("What's the next number?: "))
        
        # Third: Save the result
        result = calculate(last_answer, num3)
    
    return result

print(answer())
