# # Now we going to understand about the poly morphism in python
# x="hello World"
# print(len(x))

# # polymorphism often includes the multiple classes with the same name
# class Car:
#     def __init__(self,brand,model):
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
#         print("FLY!")
# car1=Car("Ford","Mustang")
# boat1=Boat("Ibiza","Touring 20")
# plane1=Plane("Boeing","747")

# for x in (car1,boat1,plane1):
#     x.move()
    
    
# # now we going to undestand an example of polymorphism with inheritance
# class Vechile:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("Move!")
# class Car(Vechile):
#     def move(self):
#         print("Sail!")
# class Boat(Vechile):
#     def move(self):
#         print("Fly!")
# class Plane(Vechile):
#     def move(self):
#         print("Fly!")
# car1=Car("Ford","Mustang")
# boat1=Boat("Ibiza","Touring 20")
# plane1=Plane("Boeing","747")

# for x in(car1,boat1,plane1):
#     print(x.model)
#     print(x.brand)
#     x.move()
    
    
#JSON is a syntax for storing ans exchanging the data
#JSON is a text for the JAVA SCRIPT OBJECT NOTATION
import json
x={"name":"John","age":30,"city":"New York"}
y=json.loads(x)
print(y["age"])

# dump is method that is used to conver the python to JSON

import json
x={
    "name":"John",
    "age":30,
    "city":"New York"
}
# dumps method convert the pyhton into the string
y=json.dumps(x)
print(y)


import json

x={
    "name":"John",
    "age":30,
    "married":True,
    "divorced":False,
    "children":("Ann","Billy"),
    "pets":None
}