import math


def sok(array, x):
    lengde = len(array)
    for i in range(lengde):
        if array[i] == x:
            return True
    return False


liste = [2, 3, 5, 7, 9]
target = 2
resultat = sok(liste, target)


# Vi antar at arrayet/listen er ordnet
def binaersok(array, x):
    low = 0
    high = len(array)
    while low <= high:
        i = (low + high) // 2
        i = math.floor(i)
        if array[i] == x:
            return True
        elif array[i] < x:
            low = i + 1
        elif array[i] > x:
            high = i - 1
    return False


liste2 = [2, 7, 7, 8, 11, 16, 17, 17, 20, 21, 22, 29, 31, 34, 39, 39, 41, 41, 42, 43, 45, 47, 50, 50,
          54, 58, 58, 63, 66, 68, 70, 70, 70, 70, 71, 72, 73, 75, 76, 82, 84, 85, 89, 89, 90, 97, 98, 99, 100]
target2 = 82
resultat2 = binaersok(liste2, target2)
print(resultat2)


class Node:
    def __init__(self, data=None):
        self.data = data
        self.parent = None


class lenkeliste:
    def __init__(self):
        self.start = None

    def listePrint(self):
        printStart = self.start
        while printStart is not None:
            print(printStart.data)
            printStart = printStart.parent

    def depth(self, node):
        if node == None:
            return -1
        else:
            return 1 + self.depth(node.parent)


lenkeListe = lenkeliste()


james = Node("James")
lenkeListe.start = james
karl = Node("Karl")
thomas = Node("Thomas")

lenkeListe.start.parent = karl
karl.parent = thomas

lenkeListe.listePrint()
dybde = lenkeListe.depth(thomas)
print(dybde)
