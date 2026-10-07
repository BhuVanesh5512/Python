def parse_numbers(data):
    try:
        numbers = [int(x.strip()) for x in data.split(",")]

        if len(numbers) != 2:
            return None

        return numbers

    except ValueError:
        return None


def get_input():
    data = input("Enter two numbers using comma ',': ")
    return parse_numbers(data)


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def display(result):
    if result is None:
        print("Division by zero is not allowed.")
    else:
        print(f"Division is {result}")


numbers = get_input()

if numbers is not None:
    a, b = numbers
    result = safe_divide(a, b)
    display(result)
else:
    print("Invalid input. Please enter exactly two numbers.")
    
    
    
'''
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


try:
    result = divide(10, 2)
except ValueError as error:
    print("Error:", error)
else:
    print("Result:", result)
finally:
    print("Done")
'''
