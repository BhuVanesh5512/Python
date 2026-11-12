# iterables are object we can iterate over
#iterator Which is used to iterate over iterables (for is used)
numbers = [10,20,30,40]
it = iter(numbers)
print(next(it))#10
print(next(it))#20

#generator : convenient way to create iterator and uses yield to produce value and pause its execution

def generate_numbers():
    print("Starting")
    yield 10

    print("Continuing")
    yield 20

    print("Finishing")
    yield 30


gen = generate_numbers()

print(next(gen))
print(next(gen))

def positive_numbers(numbers):
    for number in numbers:
        if number > 0 :
            yield number 
 
numbers2 = [4, -2, 0, 7, -5, 3]          
num = positive_numbers(numbers2)

print(next(num))

# numbers = [10, 20, 30]

# iterator = iter(numbers)

# print(list(iterator))
# print(list(iterator))

# iterator2 = iter(numbers)

# print(list(iterator2))