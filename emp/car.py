class Car():
    def __init__(self, wheels: int):
        self.wheels = wheels

    def __str__(self):
        return f'I am a car with {self.wheels} wheels'
