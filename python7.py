# Now we are going to learn about the iterators in Python3
# An iterator in Python is an object that consiste of th countable number of values
# An iterator is an object that can be iterated upon means u can traverse through all the values through iterator

# Iterable objects are those on which iterator can be implemented
# iterator can be applied on iterable objects to traverse then

# mytuple=("apple","banana","cherry")
# myit=iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# mystr="banana"
# myit=iter(mystr)

# print(next(myit))
# print(next(myit))
# print(next(myit))


# mystr="banana"
# myit=iter(mystr)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# # _iter_() method acts similira you can do operations but must always return the iterator object itself
# class MyNumbers:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x
# myclass=MyNumbers()
# myiter=iter(myclass)
# print(next(myiter))
# print(next(myiter))