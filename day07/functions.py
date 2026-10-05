def calculate_square(number) :
    return number**2

number  = int(input("Enter a number : "))
print(f"Square of {number} is {calculate_square(number)}")

def calculate_average(number_list):
    if not number_list:
        return 0
    total = 0
    for number in number_list:
        total +=number
    
    average = total/(len(number_list))
        
    return average

def calculate_max(number_list):
    if not number_list:
            return None
    largest = number_list[0]
    for i in range(1, len(number_list)):
        if number_list[i] > largest:
            largest = number_list[i]
            
    return largest

def calculate_min(number_list):
    if not number_list:
            return None
    smallest = number_list[0]
    for i in range(1, len(number_list)):
        if number_list[i] < smallest:
            smallest = number_list[i]
            
    return smallest


n = int(input("Enter number of elements in list : "))
number_list = []
print("Enter list of numbers one by one")
for _ in range(n):
    number_list.append(int(input()))
    
print(f"average of list {number_list} is {calculate_average(number_list)}")
print(f"Max in the list {number_list} is {calculate_max(number_list)}")
print(f"Min in the list {number_list} is {calculate_min(number_list)}")


print("="*10)
def calculate_min_max(number_list):
    if not number_list:
                return None
    smallest = number_list[0]
    largest = number_list[0]
    for i in range(1, len(number_list)):
        if number_list[i] < smallest:
            smallest = number_list[i]
    
        if number_list[i] > largest:
            largest = number_list[i]
            
    return (smallest,largest)

result = calculate_min_max(number_list)
if result is None :
    print ("The list has no elements")
else :
    print(f"The min and max values of list {number_list} are {result}")
    
print("="*20)
def calculate_min_max2(number_list):
    if not number_list:
        return None

    smallest = number_list[0]
    largest = number_list[0]

    for number in number_list[1:]:
        if number < smallest:
            smallest = number

        if number > largest:
            largest = number

    return smallest, largest
result = calculate_min_max2(number_list)
if result is None :
    print ("The list has no elements")
else :
    print(f"The min and max values of list {number_list} are {result}")

print("="*20)#scope LEGB #B is built-in name space like len(), max(), min()...

x = "global"

def local_outer():
    x = "local"
    return (x)
    
def outer():
    x = "outer"
    def inner():
        return (x)
        
    return inner()
    
print(f"Local : {local_outer()}")
print(f" global : {x}")
print(f"by enclosing : {outer()}")
print("="*10)
x = [10,20]
print(x+[10])

print("="*20)
def add(*numbers): #can collect n arguments in a tuple
    return sum(numbers)

added_result = add(1,2,3,4)
print(f"added result : {added_result}")
