# Now we learn how to perform read write 
f=open("gatik.txt","r")
print(f.read())

# if the file is located in different location then we have to specify the pathf for the file
# we can also specify the character that we have to return

f=open("gatik.txt","r")
print(f.readline())

f=open("gatik1.txt","r")
for x in f:
    print(x)
    
# Now we learn how to delete the file
# we have to import the os to delete the file

import os
os.remove("gatik.txt")


# Now learn to delete the file by checking the path
import os 
if os.path.exists("gatik2.txt"):
    os.remove("gatik2.txt")
else:
    print("The file does not exist")
    

# Now we going to learn how to write inside a file
# we have two parameters to write inside a file
# "a" will add the content to the end of the file
# "w" will over write an existing content

f=open("gatik.txt","a")
f.write("Now more content has been added to the file")
f.close()

f=open("gatik1.txt")

# Now writing to an existing file

f=open("gatik.txt","w")
f.write("Woops! I have deleted the content present inside the file")
f.close()

f=open("gatik.txt","r")
print(f.read())

# Create a new filen
# To create new file in python use the open method with pnw ov rhe followinf paraeters