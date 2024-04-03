# now we going to study about the classes and objects in python
# this is the synta for creating a class

# class Myclass:
#     x=5
# # this is the syntax for creating the object
# p1=Myclass()
# print(p1.x)

# class Person:
#     # _init_ function is called everytime automatically everytime class is being used to create a new object
#     def __init__(self,name,age,Roll):
#         self.name=name
#         self.age=age
#         self.Roll=Roll
# p1=Person("John",36,22)
# print(p1.name)
# print(p1.age)
# print(p1.Roll)


# str function is string representation of an object

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"{self.name},{self.age}"
# p1=Person("John",36)

# print(p1)

# understanding the function and print the greeting using that particular function
# self parameter is a reference to the current instance of the class is used to acess the cariables that belong to the class

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     def myfunc(self):
#         print("Hello my name is "+self.name)
# p1=Person("John",36)
# print(p1.name)
# p1.myfunc() 


# # in the case of the class the first paramter is always self paramter
# # the first parameter for any class is self parater be remember it ehile writitng

# class Person:
#     def __init__(mysillyobject,name,age):
#         mysillyobject.name=name
#         mysillyobject.age=age
#     def myfunc(abc):
#         print("Hello my name is"+abc.name)
# p1=Person("John",36)
# # Now we leanr about the modification of the objects
# p1.age=40
# p1.myfunc()
# # we can delete the properties of the object by using the del key word
# # del p1.age
# print(p1.age)


#Now understanding the inhertance in the python

# Inheritance allows us to define a class that inherita all the methods and properties from another class
# parent class is also called base class because another classes inherited from that class
# child class is the class inherited from the another class also called derived class

# class Person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
        
#     def printname(self):
#         print(self.firstname,self.lastname)
# x=Person("John", "Doe")
# x.printname()
# # Now we learn the syntax for creating the child class
# # to create a class that inherit thw functionality of the another class

# # class Student(Person):
# #     pass
# # x=Student("Mike","Olsen")
# # x.printname()
    
    
# # Now we learn about the how to add the init function inside the chid class
# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year
#   def welcome(self):
#       print("Welcome",self.firstname, self.lastname, "to the class of",self.graduationyear)
# x = Student("Mike", "Olsen", 2019)
# x.welcome()
        
        
# Now understanding abou the polymorphism in python
# class Car:
#     def __init__(self,brand,model) :
#         self.brand=brand
#         self.model=model 
    
#     def move(self):
#         print("Drive!")

# class Boat:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model  
#     def move(self):
#         print("Sail!")
        
# class Plane:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("FLy!")
        
# car1=Car("Ford","Mustang")
# boat1=Boat("Ibiza","Touring 20")
# plane1=Plane("Boeing","747")

# for x in(car1,boat1,plane1):
#     x.move()


# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Move!")

# class Car(Vehicle):
#   pass

# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")

# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang") #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747") #Create a Plane object

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()
        
          


# Now we going to learn abou the polymorphism in python
#Polymorphism in Programming refers to many forms it refers to methods functions and operators with the same name 



# poly morphism is pften used in classses where we can have multiple classes with same method name

# class Car:
#   def __init__(self,brand,model):
#     self.brand=brand
#     self.model=model
#   def move(self):
#     print("Drive!")

# class Boat:
#   def __init__(self,brand,model):
#     self.brand=brand
#     self.model=model
#   def move(self):
#     print("Sail!")
# class Plane:
#   def __init__(self,brand,model):
#     self.brand=brand
#     self.model=model
#   def move(self):
#       print("Fly!")
# car1 = Car("Ford", "Mustang")       #Create a Car class
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
# plane1 = Plane("Boeing", "747")  
# for x in (car1,boat1,plane1):
#   print(x.move())
      
      
# Now we are going to run an example in which we are going to apply the polymorphism with inheritance
class Vechile:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  def move(self):
    print("MOve")
class Car(Vechile):
  pass

class Boat(Vechile):
  def move(self):
    print("Sail!")
class Plane(Vechile):
  def move(self):
    print("FLY!")
car1=Car("Ford","Mustang")
boat1=Boat("Ibiza","Touring 20")
plane1=Plane("Boeing","747")

for x in (car1,boat1,plane1):
  print(x.brand)
  print(x.model)
  x.move()  