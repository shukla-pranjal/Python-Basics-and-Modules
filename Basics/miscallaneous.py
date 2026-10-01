c = " kkmDck"
print(c.capitalize()) #  kkmdck bcz first character is  blank space
#print(len(c.center(50)))  #50
print(c.center(50))#                      kkmDck       


print(c.endswith("ck"))   # True
print(c.startswith(" k")) # True
#endwith & startswith (string, start ,end)
print(c.startswith(" k" , 0 ,65))  #True


print(c.find(" mm")) #return first index where found
#print(c.index(" mm")) #return first index where found

print(c.rfind(" mm")) #return last index where found


#but difference is index one gives error and find gives -1 if not found

print(c.isprintable()) #retunrns true if printable else false
#like new line , backlash are not printable

# in isspace tab also considered as space








a = input("Enter first number") #a = 3
b = input("Enter second number") #b =42
print(a+b) #342

name = "Pranjal"
Pranjal = "name"

a = "!!!Pranjal!Pranjal!!!!!!!!!!!!!!!!"
b = "!!! Pranjal! Pranjal!!!!!!!!!!!!!!!!"
print(a.rstrip('!')) #!!!Pranjal
print(a.replace("Pranjal", "Kumar")) #!!!Kumar!Kumar!!!!!!!!!!!!!!!!
print(a.split(" "))# ['!!!Pranjal!Pranjal!!!!!!!!!!!!!!!!']
print(b.split(" "))#['!!!', 'Pranjal!', 'Pranjal!!!!!!!!!!!!!!!!']
#split return in string



