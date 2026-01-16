#from dataclasses import dataclass

## Magic Methods / Dunder Methods / Double Underscore
## Quad Underscore Methods
#@dataclass
class QQ():
    def __init__(self):
        self.name = "QuntumQuantified"
        self.tasks = []
        self.matrix = [[]]

    def __getitem__(self, index=0):
        return 'item'

    def __len__(self):
        return 1000000

    def __post_init__(self):
        print('post inited')

    def __repr__(self):
        return f"QQ Name is: {self.name}"

    def __add__(self, other):
        concatQQ = QQ()
        concatQQ.name = self.name + other.name
        return concatQQ

    #enumeration / yeild __iter__
    #@
    #def __@__(self, other):
    #    pass

    def __enter__(self):
        print('__enter__')

    def __exit__(self):
        print('__exit__')

    def __del__(self):
        print('__del__')

    def __new__(self):
        print('__new__')

myQQ = QQ()
myOtherQQ = QQ()

#print(myQQ + myOtherQQ)

#print(myQQ.name)
print(myQQ)

print(len(myQQ))


