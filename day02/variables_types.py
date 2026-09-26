print("="*20)
print("DataTypes")
print("="*20)

#variable are name to objects so they has type,id and value in python

age = 19
height = 5.9
name = "luffy"
is_learning = True
current_project = None

print(f" Age : {age} ")

print(f" Height : {height}")

print(f" Name : {name}")

print(f"is_learning : {is_learning}")

print(f"current_project variable : {current_project}")


print("\n\nTypes")

print(f"DataType of age variable {age} is {type(age)}")

print(f"DataType of height variable {height} is {type(height)}")

print(f"DataType of name variable {name} is {type(name)}")

print(f"DataType of is_learning variable {is_learning} is {type(is_learning)}")

print(f"DataType of current_project variable {current_project} is {type(current_project)}")

print("\n\nobject Id")

print(f"age: {id(age)}")

print("\n\n")
#mutable vs immutable curial thing

features = [10,20,30]
processed_features = features
processed_features.append(40)
print(features)# this give something we need to notice

print("\n\n identity vs equality")
print(f"equality of `features == processed_features` : {features == processed_features}")
print(f"identity of `features is processed_features` : {features is processed_features}")

#we can use type convention for compatible data values
print("\n\nTypeConvention")
age = str(age)
print(f"{age} and type : {type(age)}")

print(f"height + age : {height + int(age)}")

#boolean values true and false 
print("\nIndependent identity")
a = [1,2,3]
b = [1,2,3]
print(f"a==b : {a==b}")
print(f"a is b : {a is b}")


''' 
== asks "Do these objects compare equal?"
is asks "Are these the exact same object?" 
   
    Assignment changes what a name refers to. Mutation changes the object itself.
'''
print("\n")
print("="*20)

def doc_string():
    """
== asks "Do these objects compare equal?"
is asks "Are these the exact same object?" 
   
    Assignment changes what a name refers to. Mutation changes the object itself.
    """

print(doc_string.__doc__)