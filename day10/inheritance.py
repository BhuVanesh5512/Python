'''overriding : Create a parent class AIModel with a method predict() that returns "General prediction".
Then create a child class TextModel that overrides predict() and returns "Text prediction".
Create a TextModel instance and print its prediction.'''
class AIModel:
    def predict(self):
        return "General prediction."

class TextModel(AIModel):#inheritance
    def predict(self):
        return "Text prediction"

model1 = TextModel()
print(model1.predict())

'''ploynmorphism: Create two classes, TextModel and EmbeddingModel. Each should implement a run() method that returns a different string.
Write one function execute(model) that calls model.run() and prints the result. 
Use the same function with an instance of each class.'''
# class TextModel():
#     def run(self):
#         return "Text prediction model"

# class EmbeddingModel():
#     def run(self):
#         return "Embedding Text prediction model"
    
# def execute(model):
#     print(model.run())

# execute(TextModel())
# execute(EmbeddingModel())

#composition 
# class AIModel:
#     def run(self):
#         return "Generating output"

# class AIApplication:
#     def __init__(self, model):
#         self.model = model

#     def execute(self):
#         return self.model.run()

# app = AIApplication(AIModel())
# print(app.execute())

'''
class AIModel: #parent
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"Parent: {self.name}"


class TextModel(AIModel): #Child
    def describe(self):
        return f"Child: {self.name}"


model = TextModel("GPT")

print(model.describe())
print(isinstance(model, TextModel))
print(isinstance(model, AIModel))
'''