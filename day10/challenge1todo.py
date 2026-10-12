'''class AIModel:
    def __init__(self, name, version):
        # todo: store name on this object
        # todo: store version on this object
        pass

    def describe(self):
        # todo: return a string like:
        # "GPT - Version 1"
        pass


model1 = AIModel("GPT", 1)
model2 = AIModel("BERT", 2)

print(model1.describe())
print(model2.describe())'''

class AIModel:
    def __init__(self,name,version):
        self.name = name 
        self.version = version
        
    def describe(self):
        return f"{self.name} - Version {self.version}"
    
model1 = AIModel("GPT", 1)
model2 = AIModel("BERT", 2)

print(model1.describe())
print(model2.describe())
'''
Python creates two distinct instances.
model1
Instance of AIModel

name → "GPT"
version → 1


model2
Instance of AIModel

name → "BERT"
version → 2
'''
