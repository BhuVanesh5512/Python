
#key value pair 

dict = {
    "name" : "Luffy",
    "age" : 19
}
print(f" dictionary dict : {dict} and its type : {type(dict)}")
print("-"*10)
dict["height"] = 5.7 #adding
print(f" dictionary dict : {dict}")
dict["height"] = 5.9 #updated
print(f" dictionary dict : {dict}")
print("="*10)
print(f"name in dict {dict} : {"name" in dict}") # meembership checks only keys
print(f"Luffy in dict  {dict} : {"Luffy" in dict}") # not values
print("="*10)#retrieval
print(f"retrieving using get of dictionary {dict.get("name")}")
print(f"retrieving a key (occupation) which is not present in dictionary dict : {dict.get("occupation")}")
print(f"retrieving a key (occupation) which is not present in dictionary dict : {dict.get("occupation",0)}")
print("="*10)#iterations
for key in dict :
    print(key, end = " ")

print("\n")

for key, value in dict.items():
    print((key,value),end =" ")