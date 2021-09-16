#Dette er svaret på oppgave 1
class Teque:

    
    koe = []

    def push_back(self, x):
        self.koe.append(x)

    def push_front(self, x):
        self.koe.insert(0, x)

    def push_middle(self, x):
        l = len(self.koe) + 1
        self.koe.insert(int(l/2), x)

    def get(self, i):
        print(self.koe[i])



koen = Teque()

kommandoer = []
antallLinjer = int(input())

for i in range(antallLinjer):
    kommandoer.append(input())

for i in kommandoer:
    linjer = i.split()
    kommando = linjer[0]
    tall = int(linjer[1])
    if kommando == "push_back":
        koen.push_back(tall)
    elif kommando == "push_front":
        koen.push_front(tall)
    elif kommando == "push_middle":
        koen.push_middle(tall)
    elif kommando == "get":
        koen.get(tall)


