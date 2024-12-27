# Task 1
def greet(name):
    print(f"Hello, {name}!")

# Task 2
def print_numbers():
    numbers = list(range(1, 6))
    for num in numbers:
        print(num)

# Task 3
def double_number(num):
    return num * 2

# Task 4
def print_fruits():
    fruits = {
        "Apple": "Red",
        "Banana": "Yellow",
        "Cherry": "Red"
    }
    for fruit, color in fruits.items():
        print(f"{fruit}: {color}")

# Task 5
def print_uppercase(s):
    print(s.upper())

# Test the functions
greet("John")
print_numbers()
print(double_number(5))
print_fruits()
print_uppercase("hello")