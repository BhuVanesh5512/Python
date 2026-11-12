prompts = ["Explain Python", "Explain NumPy", "Explain AI"]
scores = [85, 90, 95]

prompt_scores = zip(prompts, scores)


print(list(prompt_scores))
for index,value  in enumerate(prompt_scores):
    print(f"{index+1}. {value[0]} -> {value[1]}")
    
    
    
for index, (prompt, score) in enumerate(
    zip(prompts, scores), start=1
):
    print(f"{index}. {prompt} -> {score}")
    

# for index,element in enumerate(prompt_scores):
#     for prompt , score in zip(prompts, scores):
#         print(f"{index}. {prompt} -> {score}")