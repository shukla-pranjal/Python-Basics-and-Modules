"""ERROR HANDLING (unexepected abnormal)
Error -> Due to program stop in Python
Execption -> (program correct) raised when some interrnal event occur change normal flow

SyntaxError	Raised by parser when syntax error is encountered. misspelled keyword missing colon or an unbalanced paranthesis
NameError	Raised when a variable is not found in local or global scope. Out of variable / Function (not found)
IndexError	Raised when the index of a sequence is out of range or other sequence types
ValueError	Raised when a function gets an argument of correct type but impro
like coverting unconvtable sting to integer when sting is not valid integer
KeyError	Raised when a key is not found in a dictionary.
AttributeError	Raised when attribute assignment or reference fails.
ImportError	Raised when the imported module is not found.
ZeroDivisionError	Raised when the second operand of division or modulo operation is zero.

try:
except IndexError as I:
except ValueError as T:
else:
finall: #always executed


Difference between except: and except Exception as e:
285

In the second you can access the attributes of the exception object:

>>> def catch():
...     try:
...         asd()
...     except Exception as e:
...         print e.message, e.args
... 
>>> catch()
global name 'asd' is not defined ("global name 'asd' is not defined",)
But it doesn't catch BaseException or the system-exiting exceptions SystemExit, KeyboardInterrupt and GeneratorExit:

>>> def catch():
...     try:
...         raise BaseException()
...     except Exception as e:
...         print e.message, e.args
... 
>>> catch()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in catch
BaseException
Which a bare except does:

>>> def catch():
...     try:
...         raise BaseException()
...     except:
...         pass
... 
>>> catch()
>>>

issubclass(BaseException, BaseException)
#>>> True
issubclass(BaseException, Exception)
#>>> False


issubclass(KeyboardInterrupt, BaseException)
#>>> True
issubclass(KeyboardInterrupt, Exception)
#>>> False


issubclass(SystemExit, BaseException)
#>>> True
issubclass(SystemExit, Exception)
#>>> False'' 
"""
"""a = input ("Enter the number: ")
print(f"Multiplication Table of {a} is : ")
try: 
  for i in range (1,11):
        print(f"{int(a)} x {i} = {int(a) * i}")
  arr = "x"
except:
  print("Invalid Input")
finally:
  print("I am easily executed")
print("End")
print(arr
#note-> try - execpt - finally only continous
#also try and execpt both are mandotory but finnaly is not mandotory
"""
"""
Enter the number: a
Multiplication Table of a is : 
Invalid Input
End
x
"""
"""#then you may why to simple execute instead of finnaly well its use in funciton
#finnaly always executed
def func1():
  try:
    l = [ 1,5,6,7]
    i = int (input("Enter the index: "))
    print(l[i])
    return 1
  except: 
    print("some error occured")
    return 0
  finally:
    print("Inside finnal") #even this written after return it will print
  print("I am always executed")
x = func1()
print(x) #Enter the index: 2
         # 6
         # Inside finnal
         # 1
"""
"""         
#CUSTOM ERROR
# you can also create self error in phython by 
# also you want intial error then to going further at future error
# raise just like (throw in cpp)
# in python cant raise error of b/w 5 and 9
a =int(input("Enter any value between 5 and 9: "))
if (a<5 or a >9):
  raise ValueError("Value shuld be between 5 and 9") 

#error come  


#you can handle your error too
#custom error can also raise by class
class CustomError(Exception):
  #any code 
  pass

"""

"""# Q) Write a code ask user such that if user type "quit" no error come 
# else error come

a = input("Enter a string: ")
if a != "quit":
  raise ValueError("Type valid string") 
"""

"""#nothing happen by "only" this 
ValueError("nOTHING IMPACRTJNJV ")

# BUT THIS IMPACT
# raise ValueError("Happen !!!")"""

# ─── assert Statement ─────────────────────────────────────────────────────────
# Used for DEBUGGING / TESTING conditions.
# Raises AssertionError if the condition is False.
# Syntax: assert <condition>, "optional message"

x = 5
assert x > 0               # passes silently
assert x > 0, "x must be positive"  # passes silently; message shown on failure

# assert x < 0, "x must be positive"  # would raise: AssertionError: x must be positive