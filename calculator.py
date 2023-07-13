import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def remainder(x, y):
    return x % y

def quotient(x, y):
    return x // y

def square_root(x):
    return math.sqrt(x)

def cube_root(x):
    return x ** (1/3)

# Main program
print("Calculator")

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Remainder")
    print("6. Quotient")
    print("7. Square Root")
    print("8. Cube Root")
    print("9. Exit")

    choice = input("Enter choice (1-9): ")

    if choice == '9':
        print("Exiting the calculator...")
        break

    if choice in ['7', '8']:
        try:
            x = float(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
    else:
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

    if choice == '1':
        result = add(x, y)
        print("Result:", result)
    elif choice == '2':
        result = subtract(x, y)
        print("Result:", result)
    elif choice == '3':
        result = multiply(x, y)
        print("Result:", result)
    elif choice == '4':
        if y == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = divide(x, y)
            print("Result:", result)
    elif choice == '5':
        result = remainder(x, y)
        print("Result:", result)
    elif choice == '6':
        if y == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = quotient(x, y)
            print("Result:", result)
    elif choice == '7':
        if x < 0:
            print("Error: Cannot calculate square root of a negative number.")
        else:
            result = square_root(x)
            print("Result:", result)
    elif choice == '8':
        result = cube_root(x)
        print("Result:", result)
    else:
        print("Invalid choice. Please try again.")

    print()
