def process_prompts(filename):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:

            # 1. Remove unnecessary whitespace
            prompt = line.strip()

            # 2. Skip empty prompts
            if not prompt:
                continue

            # 3. Yield valid prompts
            yield prompt

def validate_prompts(prompts):
    return all(prompt.strip() for prompt in prompts)
     

    
print(validate_prompts(['prompt', '', '   ', 'prompt2']))
print(validate_prompts(process_prompts('interview.txt')))
    

'''We use a generator to process the dataset lazily, reading and yielding one prompt at a time instead of loading the entire dataset into memory. 
This reduces peak memory consumption and makes the pipeline suitable for large datasets
'''

