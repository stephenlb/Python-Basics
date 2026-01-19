## Unarry Operators - + ~ * ** not(!) del
## Bitwise ~ NOT
def bitwiseNot(number: int) -> int:
    return ~number
print(bitwiseNot(10))

## Plus Unary operator MOST USELESS OPERATOR IN PYTHON
def plus(number: int) -> int:
    return +++++++++++number
print(plus(-10))

## Negative Unary operator
def negative(number: int) -> int:
    return -number
print(negative(10))

## Not Unary operator
## Type Coercion
def notOp(value):
    return not value
print(notOp(len([{}])))

## List unpack unary operator
def unpackArray(*array):
    return array
print(unpackArray(1,2,3,4,5))

## KWArgs Unary Operator
def dictionaryOp(**decliqe):
    return decliqe
print(dictionaryOp(jb98989='100',tinyrick='whazz'))

## Delete Unary Operator
def deleteCake(dictionary):
    del dictionary['cake']
    return dictionary
print(deleteCake({'cake':'🍰', 'tomatoe':'🍅'}))
