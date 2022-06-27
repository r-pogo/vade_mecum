# Classes
A class is a blueprint for creating concrete instances of real or non-real things that you want to model in your programs.  
A class encapsulates data and functionality related to the modelled object, data as attributes, and functionalities as methods.  

## Blueprint of a dog
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
# def __init__(the Dog object is assigned to the self parameter, 'Kodi', 12, 18)
# 3) The code in the constructor body is executed. We assign each parameter (name, age, weight) to an attribute with the same name in the Dog instance, using dot notation
# 4) After the constructor code is executed, python returns the Dog object as the result of calling it. In this case, the returned Dog object is assigned the variable kodi
# kodi is an instance of the class Dog as you are an instance of the class human.
# class attributes are associated with the class not the single instance, hence all the instance share the same attribute, here is "canis lupus" as this is the scientific shared by all the dogs regardless of the race, sex etc. 

kodi.bark() # using the method bark() on kodi
# 5) when we call a methode on an object, python passes that object to the method as its first argument, along with any other arguments you may have specified (barking has no additional arguments)
# 6) the method body evaluation is then carried out. The first line compares self.weight with 10. In this case, the object assigned to self is a kodi Dog object and the value of self.weight is 18, so this condition is True and the first case is executed.
# 7) the print statement is executed which prints self.name of the the object on which the barking method was performed, so it is an object named Kodi, so the display is Kodi, HAU HAU
# the method evaluation is now complete. In this case, this method does not return any value, but you can do so using return as you would with a normal function
````
___
````python
## Inheritance
# When dealing with an inheritance relationship between two classes, it is a IS-A relationship  
# CompanionDog is a Dog
class CompanionDog(Dog):
    def __init__(self, name, age, weight, owner):
        super().__init__(self, name, age, weight)
        self.owner = owner
        
    def walk(self):
        print(f"{self.name} and his guardian are going for a walk")
        
rufus = CompanionDog('Rufus', 8, 20, 'Jan')
print(f"The owner of {rufus.name} is {rufus.owner}")
rufus.bark()
# built in function `isinstance` is useful to check the IS-A relationship
if isinstance(rufus, Dog):
    print("yes is an instance of the class Dog")
else:
    print("no is not an instance of the class Dog=")
````