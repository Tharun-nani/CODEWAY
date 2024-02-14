def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y
while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'exit' to end the program")
    choice = input("Enter operation: ")
    if choice == 'exit':
        break
    if choice in ('add', 'subtract', 'multiply', 'divide'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == 'add':
            print("Result:", add(num1, num2))
        elif choice == 'subtract':
            print("Result:", subtract(num1, num2))
        elif choice == 'multiply':
            print("Result:", multiply(num1, num2))
        elif choice == 'divide':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")
