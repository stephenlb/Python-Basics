## Paint the rainbow
from rich import print

square = '█'

for r in range(50, 255, 50):
    for g in range(50, 255, 50):
        for b in range(50, 255, 50):
            style=f'bold rgb({r},{g},{b})'
            print(f'[{style}]{square}[/{style}]', end='')
