# Printing "hello"
print("hello")

# Conditional statement
if 5 > 2:
    print("Five is greater than two")
if 3>2:
    print("-----------")

# Variable assignment
x = 5
z = 3

# Commented-out code
# x = 5
# y = "John"
# print(x)
# print(y)

# Variable reassignment
x = 4
x = "sally"
print(x)

# Casting and printing data types
x = str(3)
y = int(3)
z = float(3)
print(type(x))
print(type(y))
print(type(z))

# Case sensitivity
a = 4
A = "sally"

# Variable naming conventions
# Camel Case: myVariableName
# Pascal Case: MyVariableName
# Snake Case: my_variable_name

# Assigning multiple values to variables
x = "gatik"
y = "alagh"
z = "khushi"
print(x)
print(y)
print(z)

# One value to multiple variables
x = y = z = "orange"
print(x)
print(y)
print(z)

# Unpacking a list into variables
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Concatenating strings
a = "python"
b = "is"
c = "awesome"
print(a, b, c)
print(a + b + c)

# Global and local variables
x = "awesome"
def myfunc():
    print("Python is " + x)

myfunc()

x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)

# we ca indentify the data type of a pyhton variable using type keyword
# there are total three numeric types in python
# int 
# Now we going to understand the strings in Python
print("Hello")
print("Hello")

a="Hello"
print(a)

# declaring multiple value using strings
a='''hello hi how are u 
i am good my name is
gatik hhh ndcbb ncb'''
print(a) 

a="Hello World!"
print(a[1])

# looping through strings
for x in "banana":
    print(x)
a="Hello world"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt="The best things in life are free!"
print("expensive" not in txt)

txt="The best things in life are free!"
if "free" in txt:
    print("Yes free is present")
    

thisset={"apple","banana","cherry","apple"}
print(thisset)

# set ia an inbuilt data structure in pythn that is unchangeable unordered unindexed\
# in set we can put any datatype in it
thisset={"apple","banana","cherry",True,1,2}
print(thisset)
print(len(thisset))
set1={"apple","banana","cherry"}
set2={1,5,7,9,3}
set3={True,False,False}
print(type(set1))

# We can also construct a set using set constructor
set4=set(("apple","banana","cherry"))
print(set4)

thisset={"apple","banana","cherry"}
for x in thisset: 
    print(x)
    
print("banana" in thisset)

# Now we are going to add the set items
set5={"orange","green","blue","pink"}

set5.add("brown")
print(set5)

set5.update(thisset)
print(set5)

# Now discard and remove are used to delete the set items
set6={"apple","banana","cherry"}
set6.discard("banana")
print(set6)



set7={"appple","banana","cherry","harry"}
x=set7.pop()
set7.clear()
# clear function is used to clear the whole set
print(set7)
print(x)



# We can also ceate loops by looping these sets
thisset={"apple","banana","cherry"}
for x in thisset:
    print(x)
    
    

# Now we are perforing the set  operations through functions
x = {"apple", "banana", "cherry"}
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)