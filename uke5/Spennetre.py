import heapq
from random import randint


class Node:
    def __init__(self, data):
        self.data = data
        self.besokt = False
        self.inDeg = 0
        self.naboer = []

    def __str__(self):
        penStr = str(self.data) + ": ["
        if (len(self.naboer) != 0):
            for kant in self.naboer:
                penStr += str(kant.data) + ", "
            penStr = penStr[:len(penStr) - 2]  # fjerner trailing komma
        return penStr + "]"


class Graf:
    def __init__(self, rettet):
        self.graf = {}
        self.rettet = rettet

    def leggTilKant(self, u, v):
        uNode = self.hentNode(u)
        vNode = self.hentNode(v)

        if (self.rettet):
            uNode.naboer.append(vNode)
            vNode.inDeg += 1
        else:
            uNode.naboer.append(vNode)
            vNode.naboer.append(uNode)

    def hentNode(self, data):
        if (data not in self.graf):
            self.graf[data] = Node(data)
        return self.graf[data]

    def hentTilfeldigNode(self):
        lengde = len(self.graf)
        tilfeldigTall = randint(0, lengde)
        return self.graf[tilfeldigTall]

    def __str__(self):
        penStr = ""
        for v in self.graf:
            penStr += str(self.graf[v]) + "\n"
        return penStr

    def settNoderUbesokt(self):
        for data in self.graf:
            node = self.graf[data]
            node.besokt = False

# ------------------------------------------------------------------------------
#
#   Fyll inn her:
#

    # Dybde-først søk
    def DFS(self, data):  # Data er å ta inn en node
        startNode = self.graf[data]
        #node = self.hentNode(data)
        startNode.besokt = True

        print(startNode.data)

        for node in startNode.naboer:
            if node.besokt is False:
                self.DFS(node.data)

    def DFSfull(self, G):  # Tar inn en graf
        for v in G:
            if v.besokt is False:
                self.DFS(v.data)

    # Bredde-først søk
    def BFS(self, data):
        queue = []

        startNode = self.graf[data]
        #node = self.hentNode(data)
        startNode.besokt = True
        queue.append(startNode)

        while len(queue) != 0:
            v = queue.pop(0)

            for kant in v.naboer:
                if kant.besokt is False:
                    kant.besokt = True
                    queue.append(kant)

            for v in queue:
                print(v.data)

    # Topologisk sortering
    def topologiskSortering(self):
        if (not self.rettet):
            print("ERROR: Kan ikke topologisk sortere en utrettet graf")
            return
        print("Topologisk sortering")

        stack = []
        for data in self.graf:
            node = self.graf[data]
            if node.inDeg == 0:
                stack.append(node)

        i = 0
        output = []
        while len(stack) != 0:
            node = stack.pop()
            print(str(node.data) + " -> ", end="")
            output.append(node)
            i += 1

            for nabo in node.naboer:
                nabo.inDeg -= 1
                if nabo.inDeg == 0:
                    stack.append(nabo)

        if i is len(self.graf):
            return output
        else:
            print("*STOP!* Grafen har en syklus")

    # Blir nytt for uke5
    # -------------------------------------------------

    def prim(self):
        tree = TreNode(None)
        q = []
        """
        Husk at dette er en heapq, og må derfor bruke metodene
        heappush() og heappop() for å legge til samt fjerne noder.
        """
        kostnad = []

        for node in self.graf:
            kostnad[node] = 9999999
            n = (node, None)
            heapq.heappush(q, (n, kostnad[node]))

        v = self.hentTilfeldigNode()
        kostnad[v] = 0
    # -------------------------------------------------


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


def main():
    foilGraf = Graf(False)
    foilGraf.leggTilKant("A", "D")
    foilGraf.leggTilKant("E", "F")
    foilGraf.leggTilKant("D", "E")
    foilGraf.leggTilKant("F", "G")
    foilGraf.leggTilKant("A", "B")
    foilGraf.leggTilKant("A", "C")
    foilGraf.leggTilKant("B", "C")
    foilGraf.leggTilKant("C", "D")
    foilGraf.leggTilKant("C", "F")
    foilGraf.leggTilKant("X", "Y")
    foilGraf.leggTilKant("X", "Z")
    foilGraf.leggTilKant("Y", "Z")
    print(foilGraf)

    print("\n---( Kaller på DFS )---")
    foilGraf.DFS("A")

    foilGraf.settNoderUbesokt()

    print("\n---( Kaller på BFS )---")
    foilGraf.BFS("A")
    foilGraf.settNoderUbesokt()

    foilGraf.prim()


main()
