# Polymorphism
Polymorphism is a fundamental concept in object-oriented programming (OOP) 
that allows objects of different classes to be treated as objects of a common superclass.

Polymorphism enables you to write code that can work with objects of different classes as 
long as they share a common interface, which is defined by a superclass or an interface.

Basically the same function/class being used for different types.
```python
print(len("cookies"))
7

print(len([10,20,40]))
3
```
This form of polymorphism is called generic functions or parametric polymorphism, 
because it can handle objects of many different types.

Polymorphism also refers to ad hoc polymorphism or operator overloading, 
where operators (such as + or *) can have different behavior based on the type of 
objects they’re operating on, e.g: 2 + 2 = 4 or 'poly' + 'morphism' = polymorphism.

There are two common forms of polymorphism in Python: method overriding and duck typing.
___
## Method Overriding
Method overriding occurs when a subclass provides its own implementation of a method 
that is already defined in its superclass. 
The overridden method in the subclass is called instead of the superclass method 
when the method is invoked on an instance of the subclass.

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

animal = Animal()
animal.sound()  # Output: Animal makes a sound

dog = Dog()
dog.sound()  # Output: Dog barks

cat = Cat()
cat.sound()  # Output: Cat meows
```
___
## Duck Typing
Duck typing is a concept in Python where the suitability of an object for a particular 
operation is determined by the presence of the necessary methods and attributes 
rather than the actual type of the object.
```python
class Duck:
    def sound(self):
        print("Quack!")

class Car:
    def sound(self):
        print("Vroom!")

def make_sound(obj):
    obj.sound()

duck = Duck()
car = Car()

make_sound(duck)  # Output: Quack!
make_sound(car)  # Output: Vroom!
```
In the example above, the make_sound() function takes an object as an argument 
and calls its sound() method. The function doesn't care about the actual type of 
the object but expects it to have a sound() method. 
Both Duck and Car classes satisfy this requirement and can be passed to the function.
___

