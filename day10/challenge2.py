'''
Write a class called AIModel with these requirements:
1. __init__ accepts name and temperature.
2. Store name as a normal instance attribute.
3. Implement a temperature property with a getter and setter.
4. Temperature must be between 0.0 and 1.0, inclusive.
5. Invalid temperatures must raise ValueError.
6. Create a model with temperature 0.6, change it to 0.9, and print the new temperature.
'''
# class AImodel :
#     def __init__ (self, name, temperature):
#         self.name = name
#         self.temperature = temperature
        
#     @property
#     def temperature(self):
#         return self._temperature
    
#     @temperature.setter
#     def temperature(self,value):
#         if not 0<= value <=1.0 :
#             raise ValueError("Invalid value for temperature, temperature should be between 0 and 1")
#         self._temperature = value

# try:
#     model1 = AImodel('Model A',0.6)
#     model1.temperature = 0.9
#     print(model1.temperature)
# except ValueError as error:
#     print(error)


class AIModel:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature  
        self.__challenge = 2        

    @property
    def temperature(self):
        return self._temperature                #_temperature underlying storage attribute

    @temperature.setter
    def temperature(self, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("Temperature must be a number")

        if not 0.0 <= value <= 1.0:
            raise ValueError(
                "Temperature must be between 0.0 and 1.0"
            )

        self._temperature = value

model1 = AIModel("Model A", 0.6)
print(model1.__dict__) #not suggested way
try:
    model1.temperature = 0.9
    print(model1.temperature) #temperature controlled public interface
    # print(model1.__challenge) #AttributeError: 'AIModel' object has no attribute '__challenge'
   
except ValueError as error:
    print(error)
