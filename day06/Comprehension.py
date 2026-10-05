numbers = [1,2,3,4,5] #list comprehension
result = [x*x for x in numbers]
print(f'original list : {numbers}')
print(f"result list through 1st comprehension : {result}")
result = [x+10 for x in numbers if x % 2 == 0] #comprehension with filter 
print(f"result after 2nd comprehension : {result}")
result = [x if x%2 ==0 else 0 for x in numbers] #comprehension with if/else
print(f"result after 3rd comprehension : {result}")
result = {x :x+2 for x in numbers}
print(f"result after 4th comprehension : {result}")
result = {x*2 if x%3 == 0 else x*3 for x in numbers}
print(f"result after 5th comprehension : {result}")
result = tuple(x*10 for x in numbers) # tuple with generator
print(f"result after tuple generator : {result}")
print("="*20)

records = [
    {"name": "Alice", "age": 25, "active": True, "skills": ["Python", "SQL"]},
    {"name": "Bob", "age": 17, "active": False, "skills": ["Python"]},
    {"name": "Rahul", "age": 30, "active": True, "skills": ["Python", "ML"]},
    {"name": "Sara", "age": 22, "active": False, "skills": ["SQL", "ML"]},
]
active_users = [user["name"] for user in records  if user["active"]]
skills = {skill for user in records for skill in user["skills"]}
active_users_25_plus = [user["name"] for user in records  if user["active"] and user["age"]>=25]
print(f"active users : {active_users}")
print(f"skills : {skills}")
print(f"active users above 25 : {active_users_25_plus}")

n = int(input("Enter number of elements to store in list : "))
user_list = [int(input()) for _ in range(n)]
print(f"user_list by comprehension : {user_list}")