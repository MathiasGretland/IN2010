class TreNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.forelder = None

    def setForelder(self, nyForelder):
        self.forelder = nyForelder

    def depth(self, v):
        if (self.forelder == None):
            return -1
        return 1 + self.depth(self.forelder)

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()


root = TreNode(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.printTree()
