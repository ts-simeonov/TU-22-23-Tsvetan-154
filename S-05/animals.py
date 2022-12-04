class MissingParameterError(Exception):
    pass

class InvalidParameterError(Exception):
    def __init__(self, name):
        message = f'Invalid class parameter: {name}'
        super().__init__(message)

class InvalidAgeError(InvalidParameterError):
    def __init__(self, age):
        message = f"Invalid parameter: {age}"
        super().__init__(message)

class InvalidSoundError(InvalidParameterError):
    def __init__(self, sound):
        message = f"Invalid parameter: {sound}"
        super().__init__(message)

class JungleAnimal():
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
    def make_sound(self):
        print(f"{self.name} says {self.sound}!")
    def print(self):
        pass
    def daily_task(self):
        pass
