# Task 1:
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b 

def divide(a, b):
    return a / b if b != 0 else "Error: Dvision by zero"

# Task 2 :
def calculator():
    # Asking the user for the operation and numbers
    operation = input("choose operation (+, -, *, /): ")
    num1 = float(input("Enter the first number"))
    num2 = float(input("Enter the second number"))

    # Perform operation
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2 if num2 != 0 else "Error Divison by zero"
    else: return "Error: Invalid operation"

    print("Results:", calculator())
    
# Task 3:
def calculator():
    try:
        # Ask user for operaton and number
        operation = input("Choose operation (+, -, *, /): ")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2 
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            return num1 / num2 if num2 != 0 else "Error: Division by zero"
        else: 
            return "Error Invalid operation"
    except ValueError:
        return "Error: Please valid numbers"
print("Result:", calculator())
          
    