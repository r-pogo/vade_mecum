# Classes
A class is a blueprint for creating concrete instances of real or non-real things that you want to model in your programs.  
A class encapsulates data and functionality related to the modelled object, data as attributes, and functionalities as methods.  

## Blueprint of a dog
# TODO https://inventwithpython.com/beyond/chapter17.html
````python
class Dog:
    # class attribute shared by all instances
    species = "canis lupus"
    # Constructor
    def __init__(self, name, age, weight): #2)
        # 3)
        self.name = name 
        self.age = age
        self.weight = weight
    
    def bark(self): # 5)
        # 6)
        if self.weight > 10:
            print(self.name, 'HAU HAU') # 7)
        else:
            print(self.name, 'hau hau')
            
    def human_age(self):
        age_in_human_years = self.age * 7
        return age_in_human_years
    
    def __str__(self): # works with print() or str() eg: str(kodi)
        # good for controlling how the object is represented as a string instead of
        # the place in computer memory
        # Mainly used to give an easy readable representation of your class 
        return "My name is " + self.name
    
    def __repr__(self): # when we just inspect the object this function will be called
        # or repr(kodi)
        # should be an unambiguous representation of the object
        return f"{self.__class__.__name__}({self.name}, {self.age}, {self.weight})"
        

kodi = Dog("kodi", 12, 18) # 1) 4)
print(kodi.age) # accessing kodi's attribute age 
# 1) after evoking the constructor, which happens when you give a class name with arguments in parentheses, python first creates a new empty Dog object
# 2) your arguments are then passed to the __init__ function. Another thing happen as well, python passes the new object as the first self argument
# def __init__(the Dog object is assigned to the self parameter, 'Kodi', 12, 18).
# 3) The code in the constructor body is executed. We assign each parameter (name, age, weight) to an attribute with the same name in the Dog instance, using dot notation
# 4) After the constructor code is executed, python returns the Dog object as the result of calling it. In this case, the returned Dog object is assigned the variable kodi
# kodi is an instance of the class Dog as you are an instance of the class human.
# class attributes are associated with the class not the single instance, hence all the instance share the same attribute, here is "canis lupus" as this is the scientific shared by all the dogs regardless of the race, sex etc. 

kodi.bark() # using the method bark() on kodi
# 5) when we call a methode on an object, python passes that object to the method as its first argument, along with any other arguments you may have specified (barking has no additional arguments)
# 6) the method body evaluation is then carried out. The first line compares self.weight with 10. In this case, the object assigned to self is a kodi Dog object and the value of self.weight is 18, so this condition is True and the first case is executed.
# 7) the print statement is executed which prints self.name of the the object on which the barking method was performed, so it is an object named Kodi, so the display is Kodi, HAU HAU
# the method evaluation is now complete. In this case, this method does not return any value, but you can do so using return as you would with a normal function.

# Custom objects are mutable by default.
# Attributes values can be changed dynamically:
>>> kodi.age = 10
>>> kodi.age
10

>>> kodi.species = "Felis silvestris"
>>> kodi.species
'Felis silvestris'
````
___
## `type()` function and `__qualname__` attribute

Passing an object to the built-in type() function tells us the object’s data type through its return value. 

````python
>>> type(42)  # The object 42 has a type of int.
<class 'int'>
>>> int # int is a type object for the integer data type.
<class 'int'>
>>> type(42) == int  # Type check 42 to see if it is an integer.
True
>>> type('Hello') == int  # Type check 'Hello' against int.
False
>>> 
>>> type(kodi) == Dog  # Type check kodi against Dog.
True
# Note that int is a type object and is the same kind of object as what type(42) returns, 
# but it can also be called as the int() constructor function: the int('42') function doesn’t convert the '42' string argument;  
# instead, it returns an integer object based on the argument.
````
To have a simpler, human-readable information about the type/class use the `__qualname__` or the `__name__` attribute, which all type objects have:

````python 
>>> str(type(42))  # Passing the type object to str() returns a messy string.
"<class 'int'>"
>>> type(42).__qualname__ # The __qualname__ attribute is nicer looking.
'int'
````
The `__qualname__` or `__name__`  attribute is most often used for overriding the `__repr__()` method.
`__qualname__` gives more complete information than `__name__` and therefore can be more helpful in debugging.
___
## Class Methods
Class methods are associated with a class rather than with individual objects, like regular methods are.  
You can recognize a class method in code when you see two markers: the `@classmethod` decorator and the use of  
`cls` as the first parameter.

```python
class ExampleClass:
    def exampleRegularMethod(self):
        print('This is a regular method.')
    # # it can’t modify object instance state. But can still modify class state that applies across all instances of the class.
    @classmethod
    def exampleClassMethod(cls): # cls because class is a Python keyword
        print('This is a class method.')
 
# Call the class method without instantiating an object:
ExampleClass.exampleClassMethod()

obj = ExampleClass()
# Given the above line, these two lines are equivalent:
obj.exampleClassMethod()
obj.__class__.exampleClassMethod()
```
(A. Sweigart, 2020)

Often used as a way to provide alternative constructor methods besides `__init__()`:
```python
class AsciiArt:
    # constructor accepts either a string of data or a filename that contains data
    def __init__(self, characters):
        self._characters = characters

    @classmethod  # decorator to define class method classmethod should do something that has a 
    # relationship with the class, often used to manipulate different structures of data and to instantiate objects
    def fromFile(cls, filename):
        with open(filename) as fileObj:
            characters = fileObj.read()
            return cls(characters)

    def display(self):
        print(self._characters)

    # Other AsciiArt methods would go here...

face1 = AsciiArt(' _______\n' +
                 '|  . .  |\n' +
                 '| \\___/ |\n' +
                 '|_______|')
face1.display()

face2 = AsciiArt.fromFile('face.txt')
face2.display()
```
(A. Sweigart, 2020)
___
## Static method
A static method doesn’t have a `self` or `cls` parameter. Static methods are just functions, because they can’t access the attributes or methods  
of the class or its objects.
A static method is defined by placing the `@staticmethod` decorator before their def statements.
```python
class ExampleClassWithStaticMethod:
    # This method should do something that has a relationship with the class, but not something that is unique
    # per instance!
    @staticmethod # staticmethod decorator
    def sayHello(): # First parameter is not self or cls ! You shouldn't call it from instance level. First argument is not an object no self or cls is like a regular function
        print('Hello!')

# Note that no object is created, the class name precedes sayHello():
ExampleClassWithStaticMethod.sayHello()
```
(A. Sweigart, 2020)
There would be almost no difference between the `sayHello()` static method in the `ExampleClassWithStaticMethod` class and a `sayHello()` function.
Static methods can neither access the object instance state nor the class state. They work like regular functions but belong to the class’s and every instance’s namespace.


## Sources
- A. Sweigart, Beyond the Basic Stuff with Python: Best Practices for Writing Clean Code, No Starch Press 2020
- D. Amos, Real Python, Object-Oriented Programming (OOP) in Python 3, https://realpython.com/python3-object-oriented-programming/
- E. Freeman, Head First Learn to Code: A Learner's Guide to Coding and Computational Thinking, 2019 Helion S.A

## TODO
class method and static mewthod
dunder methods
decorators - getter, setter, property
Czyanko:
https://realpython.com/operator-function-overloading/
https://realpython.com/inheritance-composition-python/
https://www.youtube.com/watch?v=upmOAPk2cK8&ab_channel=SebastiaanMath%C3%B4t
https://realpython.com/python-multiple-constructors/