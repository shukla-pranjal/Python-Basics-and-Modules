class  Employee:
    def __init__(self):
        self.name =  "Kumar"
        self.__tag = "Pranjal" # like here tag is private by __ (double undrscrore _ )
        self._car = "no"  #protected single undrscrore
          
                
    def _funName(self): #protected function

        return "Insaan"
class Student(Employee): #inherted class
    pass
    
a =   Employee()
print(a.name)# Kumar

# print(a.__tag) # Cannot be accessed directly give error 
 
# but by using name mangling be can access
# (classObject._ClassName_PrivateAttribute)

print(a.__dir__()) #['name', '_Employee__tag', '__module__', '__init__', '__dict__', '__weakref__', '__doc__', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__reduce_ex__', '__reduce__', '__getstate__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']

print(dir(a)) #['_Employee__tag', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_car', '_funName', 'name']

print(a._Employee__tag) #by this it can accessed

print(a.__module__)

obj = Student()
print(dir(obj)) #['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_funName'] 
print(obj.__dir__())


print(obj._funName())



# so in pyhton its just covection thst mean there can change of rule for somebody else
# like other programming language in pyhon its no such use 


