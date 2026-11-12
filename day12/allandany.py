prompts = [
    "Explain Python",
    "",
    "Explain machine learning",
    "   "
]

has_invalid = any(not prompt.strip() for prompt in prompts)
all_valid = all(prompt.strip() for prompt in prompts)

valid_prompts = [
    prompt.strip()
    for prompt in prompts
    if prompt.strip()
]

print("Has invalid prompt:", has_invalid)
print("All prompts valid:", all_valid)
print("Valid prompts:", valid_prompts)

# #an empty iterable contains no true elements
# #it also contains no element that violates the condition.

print(all([]))
print(any([]))

# def generate_prompts():
#     prompts = ["Hello", "Explain Python", "", "Build an AI app"]

#     for prompt in prompts:
#         print("Checking:", prompt)
#         yield prompt.strip()


# prompt_generator = generate_prompts()

# result = all(prompt_generator)

# print("All valid:", result)

# remaining = list(prompt_generator)
# print("Remaining:", remaining)