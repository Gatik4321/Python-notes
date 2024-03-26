# Now we going to understand the file hndeling in python

f=open("gatik.txt","r")

print(f.read(5))
# Now if u have to read the first two lines of the files
print(f.readline())
print(f.readline())

for x in f:
    print(x)
    
f.close() # the syntax is used to cloase the file


# Now how to delete a fie in python
# import os
# os.remove("gatik1.txt")

# we can also remove the file by applying the conditioning
import os
if os.path.exists("gatik2.txt"):
    os.remove("gatik2.txt")
else:
    print("The file does not exists")
    
    
# Now writitng inside the file is a complex task
# we have three modes for writitng inside the files 
# a append mode create if file doesnot exits
# w write mode it will overwrite the existing content present inside the file
# x it will crete the file if file doesnot exist other show an error

f=open("gatik.txt","a")
f.write("Gatik is a good boye")
f.close()

f=open("gatik.txt","r")
print(f.read())
f.close()

f=open("gatik.txt","w")
f.write("Gaaaaaaaaaaaaaaaaaaaaa")
f.close()

f=open("gatik.txt","r")
print(f.read())