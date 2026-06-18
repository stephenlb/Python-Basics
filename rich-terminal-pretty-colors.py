## Paint the rainbow
from rich import print

square = '█'
counter = 0

for i in range(100, 255, 1):
    counter += 1
    r = i if counter > 50 or counter < 100 else 0
    g = i if counter > 10 or counter < 10  else 0
    b = i if counter > 10  or counter < 0   else 0
    #r = i #if counter > 50 else r = 0
    #g = i // 4
    # = 0#i# // 2
    style=f'bold rgb({r},{g},{b})'
    print(f'[{style}]{square}[/{style}]', end='')
