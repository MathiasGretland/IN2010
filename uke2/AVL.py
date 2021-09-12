class Node:
    def __init__(self, element):
        self.element = element  # dataen som blir lagret i noden
        self.left = None  # venstre barn av v (noden)
        self.right = None  # hoyre varn av v (noden)
        # høyden til v (noden)... altså avstanden fra den noden til den dypeste løvnoden
        self.height = 0


class AVL:
    def insert(self, root, key):
        # Normal måte å legge inn nye noder på
        if not root:
            return Node(key)
        elif key < root.element:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        return self.balance(root)

    def height(self, v):
        if v is None:
            return -1
        return v.height

    def leftRotate(self, z):
        y = z.right
        T1 = y.left

        y.left = z
        z.right = T1

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def rightRotate(self, z):
        y = z.left
        T2 = y.right

        y.right = z
        z.left = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def balanceFactor(self, v):
        if v is None:
            return 0
        return self.height(v.left) - self.height(v.right)

    def balance(self, v):
        if self.balanceFactor(v) < -1:
            if self.balanceFactor(v.right) > 0:
                v.right = self.rightRotate(v.right)
            return self.leftRotate(v)

        if self.balanceFactor(v) > 1:
            if self.balanceFactor(v.left) < 0:
                v.left = self.leftRotate(v.left)
            return self.rightRotate(v)

    def remove(self, v, x):
        if v is None:
            return None
        if x < v.element:
            v.left = self.remove(v.left, x)
        elif x > v.element:
            v.right = self.remove(v.right, x)
        elif v.left is None:
            v = v.right
        elif v.right is None:
            v = v.left
        else:
            u = self.findMin(v.right)
            v.element = u.element
            v.right = self.remove(v.right, u.element)
        v.height = 1 + max(self.height(v.left), self.height(v.right))

        return self.balance(v)

    # Procedure for å finne minste løvnode
    def findMin(self, v):
        if v is None or v.left is None:
            return v
        return self.findMin(v.left)


# Parameteret v er en node
# Samme er z, men er litt mer komplisert
mittTre = AVL()
root = None

root = mittTre.insert(root, 10)
root = mittTre.insert(root, 20)
root = mittTre.insert(root, 25)
root = mittTre.insert(root, 15)
root = mittTre.insert(root, 35)
root = mittTre.insert(root, 22)
