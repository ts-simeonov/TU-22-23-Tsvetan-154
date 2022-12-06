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
        if type(name) != str:
            raise InvalidParameterError(name)
        elif type(age) != int:
            raise InvalidAgeError(age)
        elif type(sound) != str:
            InvalidSoundError(sound)
        self.name = name
        self.age = age
        self.sound = sound
    
    def make_sound(self):
        print(f"{self.name} says {self.sound}!")
    
    def print(self):
        pass

    def daily_task(self):
        pass

class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        if age > 15:
            raise InvalidAgeError(age)
        elif sound.count('r') < 2:
            raise InvalidSoundError(sound)
        super().__init__(name, age, sound)
    
    def print(self):
        print(f"Jaguar({self.name}, {self.age}, {self.sound})")
    
    def daily_task(self, animals):
        for i in animals:
            if type(i) == Lemur or type(i) == Human:
                animals.remove(i)
                print(f"{self.name} the Jaguar hunted down {i.name} the {type(i).__name__}")

class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        if age > 10:
            raise InvalidAgeError(age)
        elif sound.count('e') < 1:
            raise InvalidSoundError(sound)
        super().__init__(name, age, sound)
    
    def print(self):
        print(f"Lemur({self.name}, {self.age}, {self.sound})")
    
    def daily_task(self, fruits):
        if fruits >= 10:
            print(f"{self.name} the Lemur ate a full meal of 10 fruits")
            return fruits - 10
        elif fruits < 10:
            print(f"{self.name} the Lemur could only find {fruits} fruits")
            return 0
        elif fruits <= 0:
            self.make_sound()
            self.make_sound()
            print(f"{self.name} the Lemur couldn't find anything to eat")
            return 0

class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        if age > 10:
            raise InvalidAgeError(age)
        elif 'e' not in sound:
            raise InvalidSoundError(sound)
        super().__init__(name, age, sound)
    
    def print(self):
        print(f"Human({self.name}, {self.age}, {self.sound})")
    
    def daily_task(self, animals, buildings):
        for i in range(len(animals)):
            if type(animals[i]) == Human:
                if i == 0:
                    if type(animals[i + 1]) == Human:
                        buildings.append(Building(f'typee{i}'))
                elif i == len(animals):
                    if type(animals[len(animals) - 1]) == Human:
                        buildings.append(BuildingBuilding(f'typee{i}'))
                elif (i != 0) and (i != len(animals)):
                    if (type(animals[i - 1]) == Human) and (type(animals[i + 1]) == Human):
                        buildings.append(Building(f'typee{i}'))

class Building:
    def __init__(self, typee):
        if type(typee) != str:
            raise InvalidParameterError(typee)
        self.typee = typee

fruits = 100
animals = []
buildings = []

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]
import random

def MakeAnimal():
    z = random.randint(0,10)
    if z in range(0,4):
        n = random.randint(0, (len(names) - 1))
        a = random.randint(7, 20)
        s = random.randint(0, (len(sounds) - 1))
        animals.append(Lemur(names[n], a, sounds[s]))
    elif z in range(4,8):
        n = random.randint(0, (len(names) - 1))
        a = random.randint(7, 20)
        s = random.randint(0, (len(sounds) - 1))
        animals.append(Jaguar(names[n], a, sounds[s]))
    elif z in range(8,10):
        n = random.randint(0, (len(names) - 1))
        a = random.randint(7, 20)
        s = random.randint(0, (len(sounds) - 1))
        animals.append(Human(names[n], a, sounds[s])) 

for i in range(102):
    try:
        MakeAnimal()
    except InvalidParameterError as e:
        print(e)
    except InvalidAgeError as e:
        print(e)
    except InvalidSoundError as e:
        print(e)
print(f"The jungle now has {len(animals)} animals")

for anim in animals:
    if type(anim) == Jaguar:
        anim.daily_task(animals)
    elif type(anim) == Lemur:
        anim.daily_task(fruits)
    elif type(anim) == Human:
        anim.daily_task(animals, buildings)

print(f"The jungle now has {len(animals)} animals")

print(fruits)
print(animals)
print(buildings)