# Task 1:
def add_to_list(shopping_list):
    """Add items to the shopping list."""
    while True:
        item = input("Enter an item to add to the shopping list (or type 'done' to finish): ").strip()
        if item.lower() == 'done':
            break
        shopping_list.append(item)
        print(f"'{item}' has been added to the list. ")
    return shopping_list
shopping_list = []
add_to_list(shopping_list)
print("Your final shopping list:", shopping_list)

# Task 2:
def add_to_list(shopping_list):
    while True:
        item = input("Add item (or type 'done' to stop): ")
        if item.lower() == 'done':
            break
        shopping_list.append(item)

def remove_from_list(shopping_list):
    while True:
        if not shopping_list:
            print("List is empty.")
            break
        print("Current list:", shopping_list)
        item = input("Remove item (or type 'done' to stop.): ")
        if item.lower() == 'done':
            break
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print(f"{item} not in the list.")

shopping_list = []
add_to_list(shopping_list)
print("Final list:", shopping_list)

# Task 3:
def add (a, b):
    """Returns the sum of a and b."""
    return a + b 

def subtract(a, b):
    """Returns the difference when b is subtracted from a."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the quotient when divided by b."""
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."


