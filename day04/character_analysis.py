text = "Artificial Intelligence"

print(f"String :{text}")


print(f"Length of String : {len(text)}")

words = text.split()
print(f"Number of words in String : {len(words)}")

print(f"First character of String : {text[0]}")
print(f"Last Character of String : {text[-1]}")

cleaned_text = text.lower()
print(f"Number of times 'i' occur : {cleaned_text.count('i')}")

print(f"Text startswith Artificial : {text.startswith('Artificial')}")
print(f"Text Endwith Intelligence: {text.endswith('Intelligence')}")

print("="*20)
username = "   Bhuvanesh_Chowdary   "
name = username.strip().lower()
print(f"Username: {name}")
print(f"Length: {len(name)}")

count = 0
for i in name :
    count+=1
print(f"Length: {count}")

print("="*20)
text = "Python" 
text = text.replace("P","J")
print(text)

print("="*20)
user_message = "   WHAT IS MACHINE LEARNING???   "

cleaned_message = user_message.strip()
normalized_message = cleaned_message.lower()
normalized_message = normalized_message.replace("???", "")
words = normalized_message.split()

print(words)