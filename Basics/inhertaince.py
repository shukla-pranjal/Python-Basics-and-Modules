class Employee:
    def __init__(self , name , id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of Employee : {self.id} is {self.name}")
class Programmer(Employee): #prorammer is child class but employee is parent class
    def showLanguage(self):
        print("The default language is Python") 

e1 = Employee("Rohan das", 400)
e1.showDetails()
e2 = Programmer("Harry", 4100)
e2.showDetails()
e2.showLanguage()


# ─── __init__ Inheritance Rules ───────────────────────────────────────────────
# __init__ is called when a new object is instantiated.
# Members inside parent __init__() are accessible ONLY if parent constructor runs.
#
# Scenario                                  | Behaviour
# ------------------------------------------|--------------------------------------
# No __init__() anywhere                    | Works (Python provides default)
# Parent has __init__(), child doesn't      | Parent constructor runs automatically
# Child has __init__()                      | Parent constructor SKIPPED unless super() is called


# Example: super().__init__() + method overriding (dynamic dispatch)
class A:
    def __init__(self):
        self.multiply(15)       # calls B.multiply because obj is of type B
    def multiply(self, i):
        self.i = 4 * i

class B(A):
    def __init__(self):
        super().__init__()      # runs A.__init__, which calls self.multiply(15)
        print(self.i)           # prints 30  (2 * 15, because B.multiply is used)

    def multiply(self, i):
        self.i = 2 * i

obj = B()   # Output: 30


