import time

## For Loop
numbers = [1,2,3]
for number in numbers:
    print(number)

## while Loop loop forever
while len(numbers) > 0:
    number = numbers.pop()
    time.sleep(1)
    print(f"{number=}")
    
