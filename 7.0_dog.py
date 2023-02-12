#In Python, the self keyword represents an instance of a class.
# #It works as a handle to access the class members, such as attributes from the class methods.
# #It is the first argument to the __init__() method and is called automatically to initialize
# the class attributes with the values defined by the user.

class Dog:
    color = 'black'
    food = []

    def __init__(self, name, age): #konstruktor
        self.name = name
        self.age = age

    def __str__(self):
        info = f'I am {self.name}, I am {self.age} old'
        return info

    def bark(self):
        print("Woof woof")

my_dog = Dog("Faza", 10)
yours_dog = Dog("Burek", 2)
my_dog.bark()
yours_dog.bark()

my_dog.color = 'white'
print(my_dog.color)
print(yours_dog.color)

my_dog.food.append('bone')
my_dog.food.append('carrot')

my_dog.food = ['fish', 'salomon']

print(my_dog.food)
print(yours_dog.food)

print(id(my_dog))