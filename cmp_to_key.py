from functools import cmp_to_key
numbers = [7,2,9,4,1,6,2,5]
def sort(a, b): return a - b
print(sorted(numbers, key=cmp_to_key(sort)))
