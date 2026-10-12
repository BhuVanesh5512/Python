#parent
class AIModel:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature
        
    @property#getter
    def temperature(self):
        return self._temperature
    @temperature.setter#setter 
    def temperature(self,value):
        if isinstance(value,bool) or not isinstance(value,(int,float)):
            raise ValueError("Invalid Input,Temperature must be a number")
        if not 0.0 <= value <= 1.0:
            raise ValueError("Temperature must be between 0.0 and 1.0")
        self._temperature = value
    
    def run(self):
        return f"General AI prediction from {self.name}"
    
#child-1
class TextModel(AIModel):
    def __init__(self,parent, max_tokens):
        super().__init__(parent.name,parent.temperature)
        self.max_tokens = max_tokens
    @classmethod #too complicated just know this and use one in below
    def from_parent(cls, parent, max_tokens): #explain this 
        return cls(parent, max_tokens)
        
    def run(self):#overriding
        return f"Text generation from {self.name} (max_tokens={self.max_tokens})"
    
#child-2
class EmbeddingModel(AIModel):
    #Use super() for initialization. as inheritance AIModel contain init with temperature and name so, we can ignore init here i think
    def run(self):#overriding
        return f"Embedding generation from {self.name}"

#composition 
class AIApplication:
    def __init__(self,model):
        self.model = model
    
    def execute(self):
        return self.model.run()
    
#if I use :
''' def __init__(self,name,temperature,max_tokens):
        super().__init__(name, temperature)
        self.max_tokens = max_tokens'''#in child-1
#i need to give TextModel('GPT',0.5,50) -> so what is point of super or init from parent here I can just init all here without inheritance ?
#answer : reusable code of parent validation  #using above is simple without complications;inheritance reuses the parent’s behavior and establishes a subtype relationship
#super() lets the child delegate part of its implementation to the next class in the method resolution order.

model1 = AIModel('GPT',0.5)

model1_text = TextModel(model1,50)
model2_text = EmbeddingModel('GPT',0.3) # as this 

child1 = AIApplication(model1_text)
print(child1.execute()) 
child2 = AIApplication(model2_text)
print(child2.execute())
parent = AIApplication(model1)
print(parent.execute())
try:
    # test1 = EmbeddingModel('GPT',-0.1) Temperature must be between 0.0 and 1.0
    # test1 = AIModel('GPT',1.1) Temperature must be between 0.0 and 1.0
    # test1 = EmbeddingModel('GPT',"0.5") Invalid Input,Temperature must be a number
    # test1 = EmbeddingModel('GPT',True)   #Invalid Input,Temperature must be a number
    test1 = AIModel('GPT',0.0)
    print(test1.run())
    test2 = AIModel('GPT',1.0)
    print(test2.run())
except ValueError as error:
    print(error)
    
invalid_temperatures = [-0.1, 1.1, "0.5", True]

for value in invalid_temperatures:
    try:
        model = AIModel("GPT", value)
        print(f"Unexpected success: {value}")
    except ValueError as error:
        print(f"Correctly rejected {value!r}: {error}")
    
model = AIModel("GPT", 0.5)

try:
    model.temperature = 1.5
except ValueError as error:
    print(error)

print(model.temperature)  # Should still be 0.5

