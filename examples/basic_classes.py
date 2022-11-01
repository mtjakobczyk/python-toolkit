# Class definitions
class Human:
    def __init__(self, firstname, age):
        self.name = firstname
        self.age = age

    def greet(self):
        print(f'Hello, my name is {self.name}')


# Program
ania = Human("Ania", 27)
michal = Human("Michal", 35)

humans = [ania, michal, Human("Robert", 29)]
humans.append(Human("Eryk", 45))

totalAge = 0
for h in humans:
    h.greet()
    totalAge += h.age

print(f'Total age: {totalAge}')

# -- Output:
# Hello, my name is Ania
# Hello, my name is Michal
# Hello, my name is Robert
# Hello, my name is Eryk
# Total age: 136
