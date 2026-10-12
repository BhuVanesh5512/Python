class Model:
    framework = "PyTorch" #class attribute
    def __init__(self,name):
        self.name = name #object attributes
    
    def predicts(self,value):
        return f"{self.name} predicts {value*10}"
    

model_a = Model("Model A")#object created
print(f"model name is : {model_a.name}")
print(model_a.predicts(5))

model_b = Model("Model B")


'''
Class: Model
Shared method definition: predict()

model_a

name = "Model A"
Its own instance data


model_b

name = "Model B"
Its own instance data
'''