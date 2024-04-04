# an iterator is an object taht contain coutabbke number of values
# An iterator helps u to traverse upon ll the values
mytuple=("apple","banana","cherry")
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))


# we can also apply the iterator upon the string
mystr="banana"
myit=iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# An iterator function always have two methods
# iter function is used for the intializing but must always return the iterator object
# next methods allows us to do operation must return the next item in the seuence

class MyNumbers:
    def _iter_(self):
        self.a=1
        return self
    def _next_(self):
        x=self.a
        self.a+=1
        return x
myclass=MyNumbers()
myiter=iter(myclass)

