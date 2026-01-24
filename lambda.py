def inc(n):
    return n+1

a = [0,1,2,3,4,5,6,7,8,9,10]
for b in map(lambda x: x+1, a):
    print(b)

myLambda = lambda n:        n >= 5
def myfunction(n): return n >= 5

a_filtered = filter(lambda n: n >= 5, a)
a_filtered = filter(myLambda, a)
print(list(a_filtered))

def manipulateNumberAndAdd10(num, function):
    return function(num) + 10

doubled10 = manipulateNumberAndAdd10(10, lambda n: n * 2)
print(doubled10)

chat = [('Kyle',1200),('Torva',75),('Janlu',475),('Kevin',875)]
print('Unsorted Chat')
print(chat)
top_chat = sorted(chat, key=lambda c: -c[1])

print('Top Chat')
print(top_chat)
