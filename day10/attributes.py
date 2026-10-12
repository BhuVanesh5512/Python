#object vs class 
class AIModel:
    framework = "Python" #Class attribute

    def __init__(self, name):
        self.name = name #object instance  attribute


model1 = AIModel("GPT")
model2 = AIModel("BERT")

model1.framework = "PyTorch"
AIModel.framework = "Java"

print(model1.framework)
print(model2.framework)
print(AIModel.framework)
print(model1.__class__.framework)
print(model1.__dict__)
print(AIModel.__dict__["framework"])
del model1.framework #instance attribute deleted
print(model1.framework)

'''
Instance: model1
name
"GPT"


framework
"PyTorch"
Own attributes — take precedence during lookup
                    ^
                    |
Class lookup when an instance attribute is absent
Class: AIModel
framework
"Java"

Shared class attribute
'''