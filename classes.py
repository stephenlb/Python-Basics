

class SeqK(object):
    def __init__(self):
        super().__init__()
        self.name = "SeqK"

    def __repr__(self):
        return f"Name: {self.name}"

    def append_child(self, child):
        self.child = child
        return self.child

class RG(SeqK):
    def __init__(self):
        super().__init__()
        self.name = "Sivan"

class TinyRick(RG):
    def __init__(self):
        super().__init__()
        self.name = "TinyRick"
        

sivan = RG()
tiny = TinyRick()
seq = SeqK()

print(sivan)
print(tiny)
print(seq)

