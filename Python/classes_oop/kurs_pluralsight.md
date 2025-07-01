## Constructing an Object and Instantiation
```python
class Employee:
    pass

e = Employee()
print(e)
# <__main__.Employee object at 0x0000026120C96900>
print(e.__dict__)
{}
```
Class Functions for Constructing an Object
1)
__new__
Allocate memory for a new object and send it to the __init__ function

2) 
__init__
Receive a new object from the __new__ function asa a "self" parameter

Objects use internal dictionary to manage attributes.
```python
class Employee:
    def __init__(self):
        self.__dict__["name"] = "Elski"
        self.__dict__["age"] = 36
        self.__dict__["position"] = "developer"
        self.__dict__["salary"] = 4500

e = Employee()
print(e.__class__) # to see object class
```
```python
class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

        # The process of using the class to create a new object is known as Instantiation
e = Employee("Elski", 36, "Tester", 4500) # new employee instance
```
___
## Methods
Instance methods
```python
class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)
        
    def info(self):
        print(f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of {self.salary}.")


e = Employee("Elski", 36, "Tester", 4500) 
e.increase_salary(10)
e.info()
```
Special methods:
`__str__`: returns a readable string representation of an object.
`__repr__`: should return the official string representation of an object, meant to be used by developers not by end users.
            from the output you should be able to understand the instance, try to use `eval(repr(instance))` it should work if __repr__ is well defined.
```python
class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)
        
    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of {self.salary}."
    
    def __repr__(self):
        # return f"Employee({self.name}, {self.age}, {self.position}, {self.salary})"
        return f"Employee({repr(self.name)}, {repr(self.age)}, {repr(self.position)}, {repr(self.salary)})"
        # this second way is better as you should be able to use the output of the repr function to create a new string instance when passing for exemple in eval().

e = Employee("Elski", 36, "Tester", 4500) 
print(e)
print(repr(e))
# Employee(Elski, 36, Tester, 4500)

```
___
## Dunder Methods or Magic methods
e.__class__, e.__dict__ a lot of built-in methods have `__` on both sides.
Main reason i that to be sure they don't collide with other attributes like `self.dict = {}`

You can also implement special method s to your class like `__add__`

```
...
def __add__(self, other_e):
    return Employee("New, self.salary + other_employee.salary")

e3 = e1 + e2
# e3 = e1__.add__(e2)
```
___
## Getter and Setter + Abstraction + Encapsulation
Setter = a form of validation, does "something" before the value is assigned.
Getter = usually it just returns the value itself, is for consistency.Is like accessing the value directly.
        In some cases can be use to add additional formatting like with currencies, rounding, logging info etc.

Non Pythonic implementation:
```python
class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.set_salary(salary)
        
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)
        
    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of {self.salary}."
    
    def __repr__(self):
        # return f"Employee({self.name}, {self.age}, {self.position}, {self.salary})"
        return f"Employee({repr(self.name)}, {repr(self.age)}, {repr(self.position)}, {repr(self.salary)})"
        # this second way is better as you should be able to use the output of the repr function to create a new string instance when passing for exemple in eval().
    def get_salary(self):
        return self.salary
    
    def set_salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is 1000')
        self.salary = salary

e1 = Employee("Elski", 36, "Tester", 4500) 
e2 = Employee("Rafal", 46, "DevOps", 10500)

e1.set_salary(2000)
```

`Abstraction`: Hide implementation details. Users only need to have the interface e.g: setters 
`Encapsulation`: 1) Class instances should group related data and methods.
                 2) Hiding of data attributes which are only used for internal implementation purposes (data hiding).

Python doesn't have `Access modifiers`.
To let the user knows that some attribute is only used for internal purposes, you can prepend it with `_`

```
...
    def get_salary(self):
        return self._salary
    
    def set_salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is 1000')
        self.salary = salary

e1 = Employee("Elski", 36, "Tester", 4500) 
e2 = Employee("Rafal", 46, "DevOps", 10500)

e1.set_salary(2000)
e1._salary --> can still be accsessed but _ informs the user that this attribute is non-public.

```

`Name mangling` archived by prepending the attribute name with two underscores `__`

```
...
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is 1000')
        self.salary = salary

e1 = Employee("Elski", 36, "Tester", 4500) 
e2 = Employee("Rafal", 46, "DevOps", 10500)

e1.set_salary(2000)
e1.__salary --> if you try to reach the attribute outside the class you will get an attribute error
informing you that this attribute dosen't exsists. Python does some magic in the background = name mangling.
Outside the class scope it will have a different name. it will be _Employee__salary.
If I use this _Employee__salary I can still accsess the attribute outside the class.
```
### Getter and Setters Pythonic way + Computed properties
`@property`: are implemented as a decorator. Makes the function like a read-only data attribute.
            It also makes the getter backward compatible, methods like str and repr will use the salary property to retrieve the value from the hidden _salary

`@salary.setter`: the name of the decorated function should match the name of the attribute that you are trying to implement

```python
class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)
        
    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of {self.salary}."
    
    def __repr__(self):
        # return f"Employee({self.name}, {self.age}, {self.position}, {self.salary})"
        return f"Employee({repr(self.name)}, {repr(self.age)}, {repr(self.position)}, {repr(self.salary)})"
        # this second way is better as you should be able to use the output of the repr function to create a new string instance when passing for exemple in eval().
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is 1000')
        self._salary = salary

e1 = Employee("Elski", 36, "Tester", 4500) 
e2 = Employee("Rafal", 46, "DevOps", 10500)
e1.salary = 2000
# With the decorator @property I can call it without the ()
print(e1.salary)
```
If you only want to implement the setter:
Raise an error inside the getter method
```
@property
def password(self):
    raise AttributeError("Password is write-only")

@password.setter
def password(self, password):
    self._)password = password
```
`Computed properties` e.g: like an annual salary of an employee

```python
class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)
        
    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of {self.salary}."
    
    def __repr__(self):
        # return f"Employee({self.name}, {self.age}, {self.position}, {self.salary})"
        return f"Employee({repr(self.name)}, {repr(self.age)}, {repr(self.position)}, {repr(self.salary)})"
        # this second way is better as you should be able to use the output of the repr function to create a new string instance when passing for exemple in eval().
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is 1000')
        self._salary = salary
    
    @property
    def annual_salary(self):
        return self.salary * 12

e1 = Employee("Elski", 36, "Tester", 4500) 
e2 = Employee("Rafal", 46, "DevOps", 10500)
e1.salary = 2000
# With the decorator @property I can call it without the ()
print(e1.annual_salary)
```
### Caching:
```python
class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self._annual_salary = None
        
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)
        
    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of {self.salary}."
    
    def __repr__(self):
        # return f"Employee({self.name}, {self.age}, {self.position}, {self.salary})"
        return f"Employee({repr(self.name)}, {repr(self.age)}, {repr(self.position)}, {repr(self.salary)})"
        # this second way is better as you should be able to use the output of the repr function to create a new string instance when passing for exemple in eval().
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is 1000')
        self._annual_salary = None
        self._salary = salary
    
    @property
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary = self.salary * 12
        return self._annual_salary

e1 = Employee("Elski", 36, "Tester", 4500) 
e2 = Employee("Rafal", 46, "DevOps", 10500)
print(e1.annual_salary)
e1.salary = 2000
print(e1.annual_salary)
```
___
## Inheritance, Polymorphism + Slots
`Inheritance`: class Person (based or Parent or super class) --> is-a --> class Employee (derived or child sub class). 
`Polymorphism`: One thing can take many forms.

```python
class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

class Tester(Employee):
    def run_tests(self):
        print(f"testing is started by {self.name}...")
        print("Test are done.")

class Developer(Employee):
    # Method Overriding
    def increase_salary(self, percent, bonus=0):
        self.salary += self.salary * (percent/100)
        self.salary += bonus

e1 = Tester("Elski", 36, 1000)
e2 = Developer("Elski", 36, 1000)
e1.increase_salary(20)
e2.increase_salary(20,20) # will first run the method from its own class Method Overriding
e1.run_tests()

print(isinstance(e1, Tester)) # True
print(isinstance(e1, Employee)) # True

print(issubclass(Developer, Employee)) # True
print(issubclass(Employee, object)) # True
print(issubclass(Developer, object)) # True
```
Accessing the method from the parent class use the `super` function, no need to repeat the code: 
```python
class Developer(Employee):
    # Method Overriding
    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        # What happens in the background:
        # Employee.increase_salary(self, percent)
        self.salary += bonus
```
`super()` uses method resolution order so is better than calling the parent directly

Constructor and new attributes in child:
```python
class Developer(Employee):
    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        # What happens in the background:
        # Employee.increase_salary(self, percent)
        self.salary += bonus
```
`Slots`: provide instances with faster attribute access, reduce memory because each instance doesn't have to save the attributes in dictionary but you cannot add attributes dynamically anymore.

```python
class Developer:
    __slots__ = ("name", "age", "salary", "framework")
    def __init__(self, name, age, salary, framework):
        self.name = name
        self.age = age
        self.salary = salary
        self.framework = framework
        
e1 = Developer("Elski", 6, 1000, "Flask")
```
```python
class Employee:
    __slots__ = ("name", "age", "position", "salary")
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

class Tester(Employee):
    def run_tests(self):
        print(f"testing is started by {self.name}...")
        print("Test are done.")

class Developer(Employee):
    __slots__ = ("framework",)
    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework
    # Method Overriding
    def increase_salary(self, percent, bonus=0):
        self.salary += self.salary * (percent/100)
        self.salary += bonus
```
### MRO
to check it use `Developer.__mro__`
___
## Class Attributes and Methods
`Class Method`: when you need a method that belongs to the scope of the class but doesn't necessarily need to work with instances of that class.
`Class attribute`
`Static methods`: @staticmethod regular function declared in class but not related to the class, very bad idea.
```python
from datetime import date

class Employee:
    # Class attributes
    minimum_wage = 1000
    
    @classmethod
    def change_minimum_wage(cls, new_wage):
        if new_wage > 3000:
            raise ValueError("Company is bankrupt.")
        cls.minimum_wage = new_wage
        
    #factory function
    @classmethod
    def new_employee(cls, name, dob):
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.minimum_wage)
    
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)
        
    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of {self.salary}."
    
    def __repr__(self):
        # return f"Employee({self.name}, {self.age}, {self.position}, {self.salary})"
        return f"Employee({repr(self.name)}, {repr(self.age)}, {repr(self.position)}, {repr(self.salary)})"
        # this second way is better as you should be able to use the output of the repr function to create a new string instance when passing for exemple in eval().
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        if salary < Employee.minimum_wage:
            raise ValueError('Minimum wage is 1000')
        self._salary = salary
    
    @property
    def annual_salary(self):
        return self.salary * 12

e1 = Employee("Elski", 36, "Tester", 4500) 
e2 = Employee("Rafal", 46, "DevOps", 10500)
print(e1.minimum_wage) # instance also has access to class attributes
```
___
## Data Classes
Composition represent a `hes-a` relationship.
```python
class Project:
    def __init__(self, name, payment, client):
        self.name = name
        self.payment = payment
        self.client = client
        
    def __repr__(self):
        return f"Project(name={repr(self.name)}, payment={repr(self.payment)}, client={repr(self.client)}"

class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project

p = Project("Django app", 20000, "Globomantics")
e = Employee("Elski", 36, 1000, p)
```
`Data Classes`:
```python
from dataclasses import dataclass
# to implement slots in dataclasses after 3.10 just
@dataclass(slots=True)
class Project:
    name: str
    payment: int
    client: str
    # You can also define methods:
    def notify_client(self):
        print(f"Notifying the client about the progress of the {self.name}...")


class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project

p = Project("Django app", 20000, "Globomantics")
e = Employee("Elski", 36, 1000, p)
```
___
## Sources
- M. Prigl, Classes and Object-oriented Programming in Python 3, https://app.pluralsight.com/

