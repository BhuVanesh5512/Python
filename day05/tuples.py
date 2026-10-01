a = (30,40)
print(f"a = {a}")
print(f"datatype of a is {type(a)}")
print("="*10)
print(f"tuple indexable so a[0] : {a[0]}")
print("="*10)
# a[0] = 20 #gives typeerror
# print(a)
#tuple unpacking
x,y = a
print(f"x and y through unpacking tuple a : {x} , {y}")
#starred unpacking
# we can use star* for unpacking excess elements if we need  it also take zero/more values it makes a list

a =  (1,2,3,4) # re-binding the reference is possible in tuple
x, *middle,y = a
print (f"Star-unpacking values of a {a} : x-{x},middle-{middle},y-{y}")
a = (1,2) 
x,*middle,y = a
print (f"Star-unpacking values of a {a} with less elements : x-{x},middle-{middle},y-{y}")

