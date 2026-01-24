
class Node():
    def __init__(self, data):
        self.left  = None
        self.right = None
        self.data  = data
        self.children = [self]

    def add(self, node):
        self.children.append(node)
        node = self.walk(node)
        return
        if self.data > node.data:
            self.left = node
        else:
            self.right = node

    def __repr__(self):
        return str(list(map(lambda c: c.data, self.children)))

    def fullWalk(self, func):
        for child in self.children:
            func(child.data)
        
    def walk(self, node):
        if self.data > node.data:
            if not(node.left): return node
            return node.walk(node.left)
        else:
            if not(node.right): return node
            return node.walk(node.right)
        
rootNode = Node(1)
nodeA = Node(2)
nodeB = Node(3)
nodeC = Node(0)
nodeC = Node(0)

rootNode.add(nodeA)
rootNode.add(nodeB)
rootNode.add(nodeC)

print(rootNode)
