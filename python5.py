# Now we gong to learn abou the lambda function in python
x=lambda a:a+10
print(x(5))

x=lambda a,b:a*b
print(x(5,6))

x=lambda a,b,c:a*b*c
print(x(1,2,3))


def my_function(n):
    return lambda x:2*n

print(my_function(5))

def my_function(n):
    return lambda a:a*n

mydoubler=my_function(2)
print(mydoubler(9))


def my_function(n):
    return lambda a:a*n

mydoubler=my_function(2)
mytripler=my_function(3)

print(mydoubler(11))
print(mytripler(11))


# Now we are going to learn about the python date and timr library
import datetime

x=datetime.datetime.now()

print(x)