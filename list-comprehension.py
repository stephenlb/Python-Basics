## List Comprehension
mylist = [ x for x in range(10) ]
print(mylist)

mylist = [ x**2 for x in range(10) ]
print(mylist)

## ""Map"" iterate over lists and apply a function
mylist = [ x/100 for x in range(10) ]
print(mylist)

## ""Map + Filter"" iterate over lists and apply a function
mylist = [ x for x in range(10)  if x >= 5 ]
print(mylist)
