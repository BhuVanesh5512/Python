text = "  Artificial Intelligence is Powerful  "

print(text) #original_text

print("-"*10)
print(text.strip()) #text removing of spaces beginning and end

cleaned_text = text.strip() #cleaned text without extra beginning and end spaces
print("-"*10)
print(cleaned_text.lower())#lower case cleaned_text

print("-"*10)
print(cleaned_text.upper())#upper case cleaned_text

print("-"*10)
print(len(cleaned_text))#no of characters in cleaned_text

words = cleaned_text.split()
print("-"*10)
print(len(words))#no of words in cleaned_text

print("-"*10)
print(cleaned_text[0])#first_character

print("-"*10)
print(cleaned_text[-1])#last_character

print("-"*10)
print(cleaned_text[::-1])#reversed string or cleaned_text

print("-"*10)
print(cleaned_text.capitalize())#capitalize - first letter capital , all other lower

print("-"*10)
print(cleaned_text.title())

print("-"*10)
user_input = "   I LOVE PYTHON AND AI   "
cleaned_input = user_input.strip().lower()
processed_split_words = cleaned_input.split()
print(processed_split_words)

print("-"*10)
print(repr(text))