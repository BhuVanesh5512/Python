def calculate_max_min(*numbers):
    if not numbers :
        return None
    largest = numbers[0]
    smallest = numbers[0]
    for number in numbers[1:]:
        if smallest>number:
            smallest = number
        if largest<number:
            largest = number
        
    return largest,smallest

result = calculate_max_min(2,3,4,6)
if result is None: 
    print("no arguments given")
else: 
    print(f"Min and max : {result}")
    print(f"max : {result[0]}")
    print(f"min : {result[1]}")

numbers = [2,3,5,6]
result = calculate_max_min(*numbers)# if this goes to tuple then function no work why , unpacked by *
print(f"min and max of list : {result}")

def create_profile (**details):
    print(details)
    
profile = {
    "age" : 19,
"height" : 5.9,
"name" : "luffy"
}
create_profile(age = 19,height = 5.9,name = "luffy")
create_profile(**profile)
# we can use both in one process/function if we needed

#def create_model(name, *, temperature=0.7, max_tokens=500):
''' 
Here,
Everything after * must be supplied as a keyword argument.
'''
