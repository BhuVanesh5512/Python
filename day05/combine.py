students = [
    {"name": "Alice", "skills": ["Python", "SQL"]},
    {"name": "Bob", "skills": ["Python", "Docker"]},
    {"name": "Rahul", "skills": ["Python", "SQL", "Docker"]},
]

s=set()
for i in students:
    for key,value in i.items() :
        if key == "skills" :
            for j in value :
                s.add(j)
print(s)
print('='*20)

skills = set()

for student in students:
    for skill in student["skills"]:
        skills.add(skill)

print(skills)

print("="*10)


for i in students :
    print(f'{i["name"]} {len(i["skills"])}')

print("="*10)
    
all_skills = []

for student in students:
    all_skills.append(student["skills"]) #nested list

print(all_skills)
all_skills = []

for student in students:
    all_skills.extend(student["skills"]) #flat list

print(all_skills)

