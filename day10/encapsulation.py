class AIModel:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    @property #controls reading  #getter
    def temperature(self):
        return self._temperature #'_' specifies intended for internal use

    @temperature.setter #controls assignments #setter
    def temperature(self, value):
        if not 0.0 <= value <= 1.0:
            raise ValueError("Temperature must be between 0.0 and 1.0")

        self._temperature = value # avoid's infinite recursions


model = AIModel("GPT", 0.7)

model.temperature = 0.9
print(model.temperature)  # 0.9

model.temperature = 5.0  # Raises ValueError