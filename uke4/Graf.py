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

        while len(queue) is not 0:
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
            if node.inDeg is 0:
                stack.append(node)

        i = 0
        output = []
        while len(stack) is not 0:
            node = stack.pop()
            print(str(node.data) + " -> ", end="")
            output.append(node)
            i += 1

            for nabo in node.naboer:
                nabo.inDeg -= 1
                if nabo.inDeg is 0:
                    stack.append(nabo)

        if i is len(self.graf):
            return output
        else:
            print("G has a cycle")


#
# ------------------------------------------------------------------------------


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

    print()
    print()

    # Topologisk sortering
    morgenRutine = Graf(True)
    morgenRutine.leggTilKant("Dusj", "Undertøy")
    morgenRutine.leggTilKant("Dusj", "Sokker")
    morgenRutine.leggTilKant("Dusj", "Bukse")
    morgenRutine.leggTilKant("Dusj", "T-skjorte")
    morgenRutine.leggTilKant("Undertøy", "Bukse")
    morgenRutine.leggTilKant("Sokker", "Sko")
    morgenRutine.leggTilKant("Bukse", "Jakke")
    morgenRutine.leggTilKant("Bukse", "Sko")
    morgenRutine.leggTilKant("T-skjorte", "Jakke")
    morgenRutine.leggTilKant("Jakke", "Dra")
    morgenRutine.leggTilKant("Bukse", "Dra")
    morgenRutine.leggTilKant("Sko", "Dra")
    morgenRutine.leggTilKant("Frokost", "Pusse tenner")
    morgenRutine.leggTilKant("Frokost", "Dra")
    morgenRutine.leggTilKant("Pusse tenner", "Dra")

    # Disse to linjene skaper to sykler
    morgenRutine.leggTilKant("Sko", "Sokker")
    morgenRutine.leggTilKant("Dra", "Dusj")

    print(morgenRutine)
    print("\n---( Kaller på topologiskSortering )---")
    morgenRutine.topologiskSortering()


main()
