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
    operations = {"+": Add, "-": Subtract, "*": Multiply, "/": Divide}
    return operations

def calculate():
    """Calculate all operations and return the result"""
    print("Calculating...")

    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))

    while True:
        # Verify the current operator is on right use
        operations = search_operations()

        # Print all operators
        for x in operations:
            print(x)

        # The operator choosed
        operation_symbol = input("Please choose one: ")

        # Final result
        result_function = operations[operation_symbol]
        result = result_function(num1, num2)

        # Trying to use again the calculator
        test = input("Want to continue? (y/n): ")
        if test = "n":
            break