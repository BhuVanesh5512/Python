class AIApplication:
    def __init__(self, processor, model):
        self.model = model
        self.processor = processor
        
    def execute(self, prompt):
        cleaned_prompt = self.processor.clean_prompt(prompt)
        return self.model.run(cleaned_prompt)
class PromptProcessor :
    def clean_prompt(self, prompt):
        cleaned_prompt = prompt.strip()
        if not cleaned_prompt:
            raise ValueError("Prompt is Invalid")
        return cleaned_prompt
    
class FakeModel:
    def __init__(self):
        self.calls = 0

    def run(self, prompt):
        self.calls += 1
        return f"Result: {prompt}"
model = FakeModel()
app1 = AIApplication(PromptProcessor(), model)
app2 = AIApplication(PromptProcessor(), model)
app1.execute("Hello")
app2.execute("World")
print(model.calls)
print(app1.model is app2.model)