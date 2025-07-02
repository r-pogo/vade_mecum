# Super ()
super() = is used to give access to the methods of a parent class.  
          Returns a temporary object of a parent class when used.

```python
class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
        
class Square(Rectangle):
    def __init__(self, lenght, width): 
        super().__init__(lenght, width)
        
    def area(self):
        return self.lenght*self.width
        
class Cube(Rectangle):
    def __init__(self, lenght, width, height): # Is mainy needed if the constructor has additional arg
        super().__init__(lenght, width)
        self.height = height
    
    def volume(self):
            return self.lenght * self.width * self.height

square = Square(3,3)
cube = Cube(3,3,3)

```