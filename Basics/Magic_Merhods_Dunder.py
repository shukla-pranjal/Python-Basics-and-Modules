"""

dunder, double undersrocre
there are very few magic mnethods in phyhton like __init__ ,  __str__ , __repr__ , 
init method is a special method automatically invoked when you create new instance of class. This method 
responsible for setting up object intial state, and it is where you would  typically define any instance 
variable that you need
also called "construtor" we have discussed this method already

__str__ and __repr__ method are used to convert  an object to string  representation. str is used to when 
you want to print out an object , while
repr method used when you  want to get string respresentation of an object that can be used to recreate the object 

*   when it is not in __str__ then it goes to __repr__
    __str__ & __repr__ used in printing 


__str__  → readable for users
__repr__ → useful for developers/debugging

__len__ the len method used get  length of an object. this is useful you want to be able to find size of data structure

__eq__   # ==
__lt__   # <
__gt__   # >
__le__   # <=
__ge__   # >=
__ne__   # !=
"""



from typing import Any


class Employee:
    name = "Kumar"
e = Employee()

# print(len(e)) #Error
# print(e) #<__main__.Employee object at 0x000001C1A4925FA0>

class Employee2:
    name = "Kumar"
    def __len__(self):
        i = 0
        for c in self.name:
            i+=1
        return i
    def __str__(self):
        return f"The name of employee is {self.name} str"
    def __repr__(self):
        return f"The name of employee is {self.name} repr"
    
    
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)
    
e1 = Employee2()
print(len(e1)) # 5
print(e1) #The name of employee is Kumar str
print(str(e1)) #The name of employee is Kumar str
print(repr(e1)) #The name of employee is Kumar repr

        


