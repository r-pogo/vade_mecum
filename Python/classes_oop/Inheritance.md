# Inheritance and Composition
## The Object Super Class
Everything in Python is an object. Modules are objects,  
class definitions and functions are objects, and of course, objects created from classes are objects too.
````python
>>> class NewClass:
...     pass
...
>>> c = NewClass()
>>> dir(c)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__', '__weakref__']
# dir() returns a list of all the members in the specified object. 
# But there aren't any members in NewClass, so where is the list coming from? 
# Try:
>>> o = object()
>>> dir(o)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__']
````
As you can see, the two lists are nearly identical. There are some additional members in 
NewClass like `__dict__` and `__weakref__`, but every single member of the object class is also present in Class.
This is because every class you create in Python implicitly derives from object. You could be more explicit and write class NewClass(object), but it’s redundant and unnecessary.
___
### Exceptions Are an Exception
Every class that you create in Python will implicitly derive from object.  
The exception to this rule are classes used to indicate errors by raising an exception.
````python
>>> class MyError:
...     pass
...
>>> raise MyError()

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: exceptions must derive from BaseException
# All exceptions must derive from BaseException!
````

BaseException is a base class provided for all error types. 
To create a new error type, you must derive your class from BaseException or one of its derived classes. 
The convention in Python is to derive your custom error types from Exception, which in turn derives from BaseException.
````python
>>> class MyError(Exception):
...     pass
...
>>> raise MyError()

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyError
````
___
## How Inheritance Works (IS-A relationship)
To create a new child class, you put the name of the existing parent class in between parentheses in the class statement.
````
class ParentClass: 
    def whoAmI(self):
    print(f'Hello, I'm {self}')
            ^
            |  # Notice that in class diagrams, the arrow is drawn from the subclass pointing to the base class. 
            |  # This reflects the fact that a class will always know its base class but won’t know its subclasses.
          extends
            |
class ChildClass(ParentClass): # inherited also whoAmI()
    def someNewMethod(self):
        print('ParentClass objects don't have this method.')
            ^
            |
          extends
            |
class GrandchildClass(ChildClass):
    def anotherNewMethod(self): # inherited also whoAmI() and someNewMethod()
        print('Only GrandchildClass objects have this method.')
````
It’s common to say that parent-child classes represent “IS-A” relationships.  
A ChildClass object is a ParentClass object because it has all the same methods that a ParentClass object has,  
including some additional methods it defines. This relationship is one way: a ParentClass object is not a ChildClass object.  
If a ParentClass object tries to call someNewMethod(), which only exists for ChildClass objects (and the subclasses of ChildClass), Python raises an AttributeError.
````python
# CompanionDog is a Dog We also sometimes call a child class a subclass or derived class and call a parent class the super class or base class.
class Dog: # Parent class.
    ...
class CompanionDog(Dog): # Child class. You can also do multiple inheritance and create a "diamond structure"
    def __init__(self, name, age, weight, owner):
        super().__init__(name, age, weight) # 1)
        # this way is best for diamond structure
        # or to call the super class you can call them explicitly 
        # Dog.__init__(self, name, age, weight)
        # OR
        # super(Dog, self).__init__()
        # super() does much more than just search the parent class for a method or an attribute. 
        # It traverses the entire class hierarchy for a matching method or attribute
        self.owner = owner
        self.on_guard = False
        
    def walk(self):
        print(f"{self.name} and his guardian are going for a walk")
        
    def bark(self):  # 2) overwriting/extending the bark() method from Dog class
        if self.on_guard:
            print(f"{self.name}: I can't bark I'm on duty")
        else:
            Dog.bark(self)
            # OR
            super().bark()
            # Calling the parent's class method this way self is passed automatically
            
rufus = CompanionDog('Rufus', 8, 20, 'Jan')
print(f"The owner of {rufus.name} is {rufus.owner}")
rufus.bark()
# built in function `isinstance` is useful to check the IS-A relationship
if isinstance(rufus, Dog):
    print("yes is an instance of the class Dog")
else:
    print("no is not an instance of the class Dog=")

# Child classes can override or extend the attributes and methods of parent classes.  
# In other words, child classes inherit all of the parent’s attributes and methods but can also specify attributes and methods that are unique to themselves.
# 1) # Here we call the constructor of the Dog class. In this way, we define all the attributes common to all dogs. 
# If we didn't, we wouldn't define the name, age, and weight attributes for the instanced object.
# 2) Child classes inherit all the methods of their parent classes. But a child class can override an inherited method 
# by providing its own method with its own code. The child class’s overriding method will have the same name as the parent class’s method.
````
___
## The super() Function
Python's built-in `super()` method returns a temporary object of the superclass to help access its methods. It purpose is to avoid using the base class name explicity. It also enables yor class to inherit from multiple base classes.

A common use case is building classes that extend the functionality of previously built classes.
Calling the previously built methods with super() saves you from needing to rewrite those methods in your subclass, and allows you to swap out superclasses with minimal code changes.
```python
class Base:
    def __init__(self):
        print("I'm Base")
        
class Derived(Base):
    def __init__(self):
        print("I'm Derived")
        super().__init__() # same as Base.__init__(self)
        
child1 = Derived()

>>> "I'm Derived"
>>> "I'm Base"
```
In the example above the base class `Base` is called using  `super().__init__()`
The __init__() method is called on the base class Organism and passes a reference to the calling instance as an argument.  
This way, we could also modify the internal attributes of the self instance within the base class’ constructor.


The advantage of using `super().__init__()` compared to `Base.__init__(self)` is that you avoid calling the parent class explicitly.  
This is advantageous because it decouples the child from the parent class.  
For example, if you changed the name of the `Base` to `ParentClass`, the method using `super()` would still work.

Another basic example:
```python
class Base:
    def base_function(self, x):
        print("base_function", self, x)

class Derived(Base):
    def derived_function(self, x):
        print("derived_function", self, x)
        super().base_function(x) # instead of copy pasting print("base_function", self, x) from the base class
        # no need to put manually `self` parameter when using super()
        print("derived_function finished")

d = Derived()
d.derived_function("juns an argument")

>>> derived_function <__main__.Derived object at 0x000001E3C6DC8B50> juns an argument
>>> base_function <__main__.Derived object at 0x000001E3C6DC8B50> juns an argument
>>> derived_function finished
```
`super()` is particularly helpful in case of multiple inheritance:

```python
class Mammal:
    def eat(self):
        print('I eat')


class CanisLupus:
    def run(self):
        print("I run")


class Dog(Mammal, CanisLupus):
    def __init__(self):
        print('I am a dog Hau hau')
        super().run() # could also use self.run better for class methods
        super().eat() # could also use self.eat better for class methods
        
dog1 = Dog()

>>> I am a dog Hau hau
>>> I run
>>> I eat
```
For more in deep info see:
- https://www.youtube.com/watch?v=X1PQ7zzltz4&t=246s&ab_channel=mCoding
- https://realpython.com/python-super/
- https://rhettinger.wordpress.com/2011/05/26/super-considered-super/



# SKONCZYC

To determine which class a given object belongs to, you can use the built-in type():

>>> type(miles)
<class '__main__.JackRussellTerrier'>
What if you want to determine if miles is also an instance of the Dog class? You can do this with the built-in isinstance():

>>> isinstance(miles, Dog)
True
Notice that isinstance() takes two arguments, an object and a class. In the example above, isinstance() checks if miles is an instance of the Dog class and returns True.

Sometimes it makes sense to completely override a method from a parent class. But in this instance, we don’t want the JackRussellTerrier class to lose any changes that might be made to the formatting of the output string of Dog.speak().

To do this, you still need to define a .speak() method on the child JackRussellTerrier class. But instead of explicitly defining the output string, you need to call the Dog class’s .speak() inside of the child class’s .speak() using the same arguments that you passed to JackRussellTerrier.speak().

You can access the parent class from inside a method of a child class by using super():

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)
When you call super().speak(sound) inside JackRussellTerrier, Python searches the parent class, Dog, for a .speak() method and calls it with the variable sound.

Update dog.py with the new JackRussellTerrier class. Save the file and press F5 so you can test it in the interactive window:

>>> miles = JackRussellTerrier("Miles", 4)
>>> miles.speak()
'Miles barks: Arf'
Now when you call miles.speak(), you’ll see output reflecting the new formatting in the Dog class.

## Sources
- Al Sweigart, Beyond the Basic Stuff with Python: Best Practices for Writing Clean Code, No Starch Press 2020
- Isaac Rodriguez, Real Python, Inheritance and Composition: A Python OOP Guide, https://realpython.com/inheritance-composition-python/
- E. Freeman, Head First Learn to Code: A Learner's Guide to Coding and Computational Thinking, 2019 Helion S.A
