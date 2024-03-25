# Now we will study bout the python dictionaries
# items of dictionaries are ordered changeable but duplicates in the dictionaries are not allowes
thisdic={
    "brand":"Ford",
    "model":"Mustand",
    "year":1964
}
print(thisdic)

thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}


# We can acess the items of the dctionary in this way
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(thisdict["brand"])
# Now printing the length of the dictionaries
print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(thisdict))
print(thisdict["colors"])

# We can also construct  dictionary using a dict constructor
thisdict=dict(name="John",age=36,country="Norway")
print(thisdict)


# now we understand the filehandeling in python
# File is an importtant part of the web application
# Python has several functions create update delete and reading
# open function has two parameters w a r x
f=open("gatik.txt")

# Now we going to understand how to perform the read operation in the fies
f=open("gatik.txt","r")
print(f.readline())

f=open("gatik1.txt","r")
for x in f:
    print(x)
# close function is used to close the file as u can see
f.close()


import os
os.remove("gatik.txt")

import os
if(os.path.exists("gatik.txt")):
    os.remove("gatik.txt")
else:
    print("The file does not exits")
    
    

# now we are going to learn the write operation in fil in python
f=open("gatik.txt","x")
f.write("Gatik is a Good Boy")
f.close()

f=open("gatik.txt","a")
f.write("Gatik is a Good Boffey")
f.close()

f=open("gatik.txt","r")
print(f.read())