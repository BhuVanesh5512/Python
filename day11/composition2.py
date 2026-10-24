class TextModel:
    def run(self, prompt):
        return f"Text response: {prompt}"


class EmbeddingModel:
    def run(self, prompt):
        return f"Embedding generated for: {prompt}"
    
class FakeModel:
    def run(self, prompt):
            return f"fake model generated for: {prompt}"
    
''' Write an AIApplication class that receives a model through __init__().
Store that model as an instance attribute.
Write execute(self, prompt) so that it returns the result of calling the supplied model's run() method.
Create two applications: one using TextModel() and another using EmbeddingModel().
Call both applications with "Explain vector databases" and print the results.
'''
class AIApplication:
    def __init__(self,model):
        self.model = model
    
    def execute(self,prompt):
        return self.model.run(prompt)
    

app1 =AIApplication(TextModel())
app2 =AIApplication(EmbeddingModel())
app3 = AIApplication(FakeModel())


print(app1.execute('Explain vector databases'))  
print(app2.execute("Explain vector databases"))
print(AIApplication(TextModel()).execute("Explain vector databases"))
print(app3.execute("Explain vector databases"))

class PromptProcessor:
    def prepare(self, prompt):
        prompt = prompt.strip()

        if not prompt:
            raise ValueError("Prompt cannot be empty")

        return prompt


class TextModel:
    def run(self, prompt):
        return f"AI response: {prompt}"


class AIApplication:
    def __init__(self, processor, model):
        self.processor = processor
        self.model = model

    def execute(self, prompt):
        prepared_prompt = self.processor.prepare(prompt)
        return self.model.run(prepared_prompt)


app = AIApplication(PromptProcessor(), TextModel())

print(app.execute("  Explain embeddings  "))