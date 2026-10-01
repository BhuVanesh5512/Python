scores = [75, 82, 91]

scores.append(88)
scores[0] = 78
scores.extend([95,97])

print(scores)
print(len(scores))

'''
append(x) adds x itself as one element to the end of the list.
extend(iterable) iterates over the iterable and adds each of its elements to the end of the list.
'''

print("="*20)
numbers = [10, 20, 30, 40, 50]
print(numbers)
numbers.insert(1,15)
print("="*10)
print(numbers)
numbers.remove(40)
print("="*10)
print(numbers)
last = numbers.pop()
print("="*10)
print(numbers)
print(f"popped element {last}") # pop element
print(f"30 in numbers : {30 in numbers}")

print("="*20)
x = [20,30]
x.extend("AI")
print(f"string with extend gives {x} ") # gives [20,30,"A","I"] why  #string is a iterable of characters

print("="*20)
a = [[1,2],[3,4]]
b = a.copy()
b[1].append(5)
print(a)
print(b)

print(f"a is b : {a is b}")# checks outer list # dimension lists
print(f"a[0] is b[0] : {a[0] is b[0]}")#inner list remains same identical
print("-"*10)
# Rebinding/replacing the outer list element creates a new inner list.
b[0] = [10, 20]
print(f"a list : {a}")
print(f"b list : {b}")
#unpacking
a = [9,10,11]
x,y,z = a
print(f"unpacking list a {a} with x,y,z {x},{y},{z}")
