# Encapsulation
Is the idea of wrapping variables and methods within one unit. It can put restrictions
on accessing variables and methods directly and can prevent the accidental modification of data.
To prevent accidental change, an object’s variable can only be changed by an object’s method. 
Those types of variables are known as private variables.

Real word example could be a vending machine that sells sweets and coffee.
The user can interact wit the machine by pressing buttons and inserting coins, 
these are the method available for the user, but the machine itself has other internal methods and
"variables" (in this case as variables maybe we could consider the various items
eg.g to make a coffee we have a variable water, milk and coffee powder), with which the user cannot interact
but the machine uses to process the request.
___
## Private Attributes and Private Methods
Classes should only expose those attributes and methods that are relevant to the external object
caller, that is, those that make up their interface. All attributes that are not part of
object interface should be preceded by a single underscore.
```python
# Private attribute
class BankAccount:
    def __init__(self, first_name, last_name, initial_balance):
        self.first_name = first_name
        self.last_name = last_name
        self._balance = initial_balance
# ---snip---
```
```python
# Private method
import JIRA
class JiraUmp(JIRA):
    def __init__(self, usr: str, psswd: str) -> None:
        super().__init__(
            server="https://www.samsungmobilecoworking.com/its/",
            auth=(usr, psswd)
        )
        self.usr = usr

    def _get_issue_for_assignee(self, assignee: str or None,
                                capsule: str or None) -> list:
        if assignee is None:
            assignee = f'assignee={self.usr}'
        if capsule is None:
            jql = f'project=UMP AND {assignee} AND status="To Do"'
        else:
            jql = f'project=UMP AND {assignee} AND status="To Do" AND component={capsule}'

        # maxResults=False allows to go beyond the limit of 1000
        issues_in_proj = self.search_issues(jql,
                                            maxResults=False)
        list_of_issues = []
        # e.g.: of item 'UMP-173940, Chiama Mamma, viv.phoneApp'
        for issue in issues_in_proj:
            ok = f"{issue.key}, {issue.fields.summary}, {issue.fields.components[0]}"
            list_of_issues.append(ok)

        return list_of_issues
    
    def find_bixby(self, assignee: str or None, capsule) -> None:
        ump_tickets = self._get_issue_for_assignee(assignee, capsule)
        print("\nBixby error:")
        control_list_no_bixby = []
#---snip---
#TODO wziać tą częśc z pracy
```
Using too many private methods and attributes could be a sign that a class is executing
too many tasks and violates the principle of single responsibility. It could be
a sign that some of their duties must be distinguished into cooperating classes.
### Name mangling
```python
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23  # private attribute just a convention
        self.__baz = 42
        '''here there Python interpreter actually applies name mangling it changes
        changes the name of that variable in order to make it harder to create collision
        when the class is extended'''
        
t = Test()
t
<__main__.Test object at 0x000002969B0C7FA0>
dir(t)
['_Test__baz', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
 '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
 '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
 '__str__', '__subclasshook__', '__weakref__', '_bar', 'foo']
'''We can see '_bar' and 'foo' but no '__baz', that's because it was changed by the python interpreter
to _Test__baz, python does that to prevent naming collision for example if we extend the class Test()
with a subclass, because maybe you want to use the same nam in the subclass'''
```
___
## Properties
Properties allow you to run some specific code each time an object’s attribute is read, modified, or deleted.
An attribute set as private in python is just a convention, technically they are still public - they're 
accessible to code outside the class.

But you can prevent accidental invalid changes to these private attributes with properties.
In Python, properties are attributes that have specially assigned getter, setter, and deleter methods 
that can regulate how the attribute is read, changed, and deleted.

The most common need for using properties is to validate data or to make sure it’s in the format you 
want it to be in.
If you’ve thought, “I wish I could run some code each time this attribute was accessed, modified with an 
assignment statement, or deleted with a del statement,” then you want to use properties.

### Properties with decorator
Python’s property() is the Pythonic way to avoid formal getter and setter 
methods in your code. This function allows you to turn class attributes 
into properties or managed attributes.

Here the code outside the class never directly accesses the `_someAttribute` attribute 
it’s private, after all.  
Instead, the outside code accesses the someAttribute property. 
What this property actually consists of is a bit abstract: the getter, setter, and deleter 
methods combined make up the property.  
When we rename an attribute named `someAttribute` to `_someAttribute` while 
creating getter, setter, and deleter methods for it, we call this the `someAttribute property`.
In this context, the `_someAttribute attribute` is called a `backing field` or `backing variable` and 
is the attribute on which the property is based.
```python
class ClassWithProperties:
    def __init__(self):
        self.someAttribute = "some attribute"

    @property
    def someAttribute(self):  # getter or accessor
        return self._someAttribute

    @someAttribute.setter
    def someAttribute(self, value):  # setter or mutator
        self._someAttribute = value

    @someAttribute.deleter
    def someAttribute(self):  # deleter
        del self._someAttribute

obj = ClassWithProperties()
print(obj)  # "some attribute"
obj.someAttribute = "changed value"
print(obj.someAttribute)  # "changed value"
del obj.someAttribute  # deletes attribute someAttribute
```

The code in the property’s getter, setter, and deleter methods acts on the backing variable directly. 
You don’t want the getter, setter, or deleter methods to act on the property, 
because this could cause errors. In one possible example, 
the getter method would access the property, causing the getter method to call itself, 
which makes it access the property again, causing it to call itself again, 
and so on until the program crashes. 
```python
class ClassWithBadProperty:
    def __init__(self):
        self.someAttribute = 'some initial value'

    @property
    def someAttribute(self):  # This is the "getter" method.
        # We forgot the _ underscore in `self._someAttribute here`, causing
        # us to use the property and call the getter method again:
        return self.someAttribute  # This calls the getter again!

    @someAttribute.setter
    def someAttribute(self, value):  # This is the "setter" method.
        self._someAttribute = value

obj = ClassWithBadProperty()
print(obj.someAttribute)  # Error because the getter calls the getter.
```

To prevent this recursion, the code inside your getter, setter, and deleter methods should always act on 
the `backing variable` (which should have an underscore prefix in its name), never the property. 
Code outside these methods should use the property, although as with the private access underscore prefix 
convention, nothing prevents you from writing code on the backing variable anyway.

The most common need for using properties is to validate data or to make sure it’s in the format you 
want it to be in.

```python
class WizCoinException(Exception):
2     """The wizcoin module raises this when the module is misused."""
    pass

class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """Create a new WizCoin object with galleons, sickles, and knuts."""
3         self.galleons = galleons
        self.sickles  = sickles
        self.knuts    = knuts
        # NOTE: __init__() methods NEVER have a return statement.

--snip--

    @property
4     def galleons(self):
        """Returns the number of galleon coins in this object."""
        return self._galleons

    @galleons.setter
5     def galleons(self, value):
6         if not isinstance(value, int):
7             raise WizCoinException('galleons attr must be set to an int, not a ' + value.__class__.__qualname__)
8         if value < 0:
            raise WizCoinException('galleons attr must be a positive int, not ' + value.__class__.__qualname__)
        self._galleons = value
```

All Python objects automatically have a __class__ attribute, which refers to the object’s class object. 
In other words, value.__class__ is the same class object that type(value) returns. 
This class object has an attribute named __qualname__ that is a string of the class’s name. 
Specifically, it’s the qualified name of the class, which includes the names of any classes the class 
object is nested in. 
For example, if value stored the date object returned by datetime.date(2021, 1, 1), 
then value.__class__.__qualname__ would be the string 'date'. The exception messages use 
value.__class__.__qualname__ 7 to get a string of the value object’s name. 
The class name makes the error message more useful, because it identifies not only that 
the value argument was not the right type, but what type it was and what type it should be.
### Read only properties
# TODO
Your objects might need some read-only properties that can’t be set with the assignment operator =. 
You can make a property read-only by omitting the setter and deleter methods.
# TODO streszczenie + https://realpython.com/python-property/#getting-started-with-pythons-property
https://realpython.com/python-property/

