class FakeModel:
    def run(self, prompt):
        return f"Fake result: {prompt}"

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
    
app = AIApplication(PromptProcessor(), FakeModel())

result = app.execute("  Hello  ")

assert result == "Fake result: Hello"  #for only validation of expected output
print("PASS:", result)