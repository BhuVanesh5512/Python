
class PromptProcessor :
    def clean_prompt(self, prompt):
        cleaned_prompt = prompt.strip()
        if not cleaned_prompt:
            raise ValueError("Prompt is Invalid")
        return cleaned_prompt


class TextModel:
    def run(self, prompt):
        return f"Text response: {prompt}"


class EmbeddingModel:
    def run(self, prompt):
        return f"Embedding generated for: {prompt}"
    
class FakeModel:
    def run(self, prompt):
            return f"fake model generated for: {prompt}"
    
class AIApplication:
    def __init__(self, processor, model):
        self.model = model
        self.processor = processor
        
    def execute(self, prompt):
        cleaned_prompt = self.processor.clean_prompt(prompt)
        return self.model.run(cleaned_prompt)


    
app = AIApplication(PromptProcessor(), TextModel())
app1 = AIApplication(PromptProcessor(), EmbeddingModel())
app2 = AIApplication(PromptProcessor(), FakeModel())
apps = [app,app1,app2]
# prompt = input("Enter the prompt : ")
# for test_app in apps:
#     try :
#         result = test_app.execute(prompt)
#         print(f"{type(test_app.model).__name__}")
#         print(f"{result}")
#     except ValueError as err:
#         print(err)
        
# test_prompts = ["Explain Python", "", "   "]

# for test_prompt in test_prompts:
#     for test_app in apps:
#         try:
#             result = test_app.execute(test_prompt)
#             print(f"{type(test_app.model).__name__}: {result}")
#         except ValueError as err:
#             print(f"Invalid prompt: {err}")
