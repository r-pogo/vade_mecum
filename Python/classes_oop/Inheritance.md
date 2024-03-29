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
___
## Composition (HAS-A relationship)
In composition, a class known as composite contains an object of another class known to as component. 
In other words, a composite class has a component of another class.

When to an attribute is assigned another object, we speak of a HAS-A relationship. 
If we have a class called House and its objects have an attribute with the object Kitchen assigned to it, 
we can say Home HAS-A Kitchen.

```python
class Kitchen:
   # composite class constructor
    def __init__(self):
        print('Component class kitchen created')
  
    # composite class instance method
    def fridge(self):
        print("fridge is on")

class House:
    # composite class constructor
    def __init__(self):
  
        # creating object of component class
        self.kitchen = Kitchen()
  
     # composite class instance method
    def rooms(self):
        # calling fridge() method of component class
        self.kitchen.fridge()
```
Another example Employee has a Salary:
```python
class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name=name
        self.age=age
        self.obj_salary=Salary(pay, bonus)  # instantiation of Salary class

    def total_salary(self):
        return self.obj_salary.annual_salary()
    
class Salary:
    def __init__(self, pay, bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_salary(self):
       return (self.pay*12) + self.bonus

emp = Employee('Raf', 34, 5700, 1000)
print(emp.total_salary())
```
___
## isinstance() and issubclass()
The isinstance() function will return True if the object is of the given class or a subclass of the given class.

```python
>>> class ParentClass:
...     pass
...
>>> class ChildClass(ParentClass):
...     pass
...
>>> parent = ParentClass() # Create a ParentClass object.
>>> child = ChildClass() # Create a ChildClass object.
>>> isinstance(parent, ParentClass)
True
>>> isinstance(parent, ChildClass)
False
>>> isinstance(child, ChildClass)
True
>>> isinstance(child, ParentClass)  # this make sense because we have an IS-A relationship 
True
```
(A. Sweigart, 2020)

You can also pass a tuple of class objects as the second argument to see whether the first argument is one of any of the classes in the tuple:
```python
>>> isinstance(42, (int, str, bool)) # True if 42 is an int, str, or bool.
True
```
(A. Sweigart, 2020)

issubclass() built-in function can identify whether the class object passed for the first argument is a subclass of (or the same class as) the class object passed for the second argument:
```python
>>> issubclass(ChildClass, ParentClass) # ChildClass subclasses ParentClass.
True
>>> issubclass(ChildClass, str) # ChildClass doesn't subclass str.
False
>>> issubclass(ChildClass, ChildClass) # ChildClass is ChildClass.
True
```
You can pass a tuple of class objects as the second argument to issubclass() to see whether the first argument is  
a subclass of any of the classes in the tuple.  
The key difference between isinstance() and issubclass() is that issubclass() is passed two class objects, whereas isinstance() is  
passed an object and a class object.
(A. Sweigart, 2020)
___
## Multiple Inheritance
Multiple inheritance means a class can inherit from two or more parent classes.

```python
class ClassA:
    def method_a(self):
        print("Method A from ClassA")

class ClassB:
    def method_b(self):
        print("Method B from ClassB")

class ClassC(ClassA, ClassB):
    def method_c(self):
        print("Method C from ClassC")

obj = ClassC()
obj.method_a()  # Output: Method A from ClassA
obj.method_b()  # Output: Method B from ClassB
obj.method_c()  # Output: Method C from ClassC

```
It's worth noting that in case of naming conflicts between methods or attributes inherited from 
different parent classes, the method resolution order (MRO) determines which method will be called. 
The MRO defines the order in which Python searches for methods in the inheritance hierarchy. 
The `super()` function is commonly used to invoke the parent class's method in such cases.
___
## MRO
Method Resolution Order (MRO) is the order in which Python searches for methods in a class 
hierarchy during method invocation. It determines the precedence of methods when a class 
inherits from multiple parent classes, especially in the case of multiple inheritance.

Python uses the C3 linearization algorithm to calculate the MRO. 
The algorithm ensures that the order of method resolution follows a consistent 
and predictable pattern. The MRO is represented as a linear list of classes, 
where each class appears only once.

```python
class ClassA:
    def method(self):
        print("Method A from ClassA")

class ClassB(ClassA):
    def method(self):
        print("Method B from ClassB")

class ClassC(ClassA):
    def method(self):
        print("Method C from ClassC")

class ClassD(ClassB, ClassC):
    pass

```
In this example, we have four classes: ClassA, ClassB, ClassC, and ClassD. ClassD 
inherits from both ClassB and ClassC, which, in turn, inherit from ClassA.

Let's create an instance of ClassD and call the method():

```python
obj = ClassD()
obj.method()

Method B from ClassB
```

Here's how the MRO is calculated for ClassD:

1. The MRO for ClassD starts with the class itself: [ClassD].
2. The MRO includes the classes in the order they are listed in the inheritance declaration, 
from left to right: [ClassD, ClassB, ClassC].
3. The MRO includes the MROs of the parent classes (excluding duplicates) in the same order, 
respecting the left-to-right order of the inheritance declaration. In this case, [ClassD, ClassB, ClassA, ClassC, ClassA]. Note that ClassA appears twice because it's inherited by both ClassB and ClassC.
4. Finally, the duplicate classes are removed while maintaining their order, 
resulting in the MRO: [ClassD, ClassB, ClassA, ClassC].

When a method is invoked on an instance of ClassD, Python searches for the 
method in the classes according to their order in the MRO. 
It starts with ClassD, then goes to ClassB, followed by ClassA, and finally ClassC. 
If the method is found in any of the classes, it is executed. 
If the method is not found, Python raises an AttributeError.

In the example above, since ClassB comes before ClassA in the MRO, the method method() from ClassB is called. 
If you change the order of inheritance for ClassD (class ClassD(ClassC, ClassB)), 
the output will be different as the MRO changes accordingly

DODAC czesc z ksiazki!!!

## Sources
- Al Sweigart, Beyond the Basic Stuff with Python: Best Practices for Writing Clean Code, No Starch Press 2020
- Isaac Rodriguez, Real Python, Inheritance and Composition: A Python OOP Guide, https://realpython.com/inheritance-composition-python/
- E. Freeman, Head First Learn to Code: A Learner's Guide to Coding and Computational Thinking, 2019 Helion S.A
- K. Stratis, Real Python, Supercharge Your Classes With Python super(), https://realpython.com/python-super/
