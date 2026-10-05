def get_number_list():
    number_list = []
    n = int(input("Enter number of elements in list : "))
    print("Enter numbers in list one by one by pressing enter")
    for i in range(n):
        number_list.append(int(input()))
    
    return number_list

def calculate_average():
    numbers = get_number_list()
    if not numbers :
        return None
    return sum(numbers)/len(numbers) 

def display_result():
    result = calculate_average()
    if result is None:
        return "there are no elements in list"
    else:
        return result
    
print(f"average of list is {display_result()}")


'''
Above code is like a single function reaching out to get what it require this is not good 
'''
        
print("="*30)
#improved 

def get_number_list():
    number_list = []
    n = int(input("Enter number of elements in list: "))

    print("Enter numbers in list one by one:")

    for _ in range(n):
        number_list.append(int(input()))

    return number_list


def calculate_average(numbers):
    if not numbers:
        return None

    return sum(numbers) / len(numbers)


def display_result(result):
    if result is None:
        return "There are no elements in the list."

    return result


numbers = get_number_list()
result = calculate_average(numbers)

print(f"Average of list is {display_result(result)}")

'''
Above function is the improved and good written function we provide what function needed .

'''