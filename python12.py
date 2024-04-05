# Now going to learn about the exception handeling i  python

#try blocks lets u to handle the error 
# except block lets you to handle the error 
# else blocks lets u excute code when there is no error 
# finally block lets you execute code regardless of result of 

# x=5
try:
    print(x)
except NameError:
    print("An errror occured")
except:
    print("Something else went wrong")
    
# else block will execute only when there is no error

# Now we are going to write a program to execute try catch throw and except

x=5
try:
    print(x)
except:
    print("Something went wrong")
else:
    print("Code written by u is correct ad there is no error")
finally:
    print("The try except is finished")


# Now using try catch except else block in the file handeling

# try:
#     f=open("gatik.txt","r")
#     try:
#         f.write("Lorum Ipsum")
#     except:
#         print("Something went wrong with this File")
#     finally:
#         print("try and catch block executed succesfully")


# Now we going lo learn about the python functions

# A functions is a block of code which only runs when it is called 
# You can pass data known as th paraeters
def my_function():
    print("Hello from a function")

my_function()


# Now how to pass the arguments in the functions
def my_function(fname):
    print(fname+"Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# No. of arguments in the functions should always be eual to the no. of pass argumrets
# if we do not no how many operators get passe just we have to use * operator
def my_function(*kids):
    print("The youngest child is",kids[2])
my_function("gatik","gatik1","gatik3")


# Now we are going to learn about the lambda function
x=lambda a:a+10
print(x(5))

x=lambda a,b:a*b
print(x(5,6))

x=lambda a,b,c:a+b+c
print(x(5,6,2))

# lambda function are better defined when u used a function inside a function
def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(2)
print(mydoubler(2))

# Now writing a mytripler function using the lambda function

def myfunc(n):
    return lambda a:a*n

mytripler=myfunc(3)
print(mytripler(11))