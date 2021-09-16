#Dette er svaret på oppgave 1
class Node:
    element = None
    neste = None
    forrige = None

    def __init__(self, e) -> None:
        self.element = e

class Teque:

    lengde = 0

    start = None
    slutt = None
    midt = None

    def push_back(self, x):
        ny = Node(x)
        if not self.start:
            self.start = ny
            self.midt = ny
            self.slutt = ny
        else:
            temp = self.slutt
            self.slutt.neste = ny
            self.slutt = ny
            self.slutt.forrige = temp
            
            if not self.lengde % 2 == 0:
                self.midt = self.midt.neste

        self.lengde+=1
        
    def push_front(self, x):
        ny = Node(x)
        if not self.start:
            self.start = ny
            self.midt = ny
            self.slutt = ny
        else:
            ny.neste = self.start
            self.start.forrige = ny
            self.start = ny

            if self.lengde % 2 == 0: 
                self.midt = self.midt.forrige
        
        self.lengde += 1

    def push_middle(self, x):
        ny = Node(x)
        if not self.start:
            self.start = ny
            self.midt = ny
            self.slutt = ny
        else:
            if self.lengde % 2 == 0: #sette til venstre for midt og oppdatere peker til ny
                tmp = self.midt  # tidligere mid peker
                tmp.forrige.neste = ny
                ny.forrige = tmp.forrige
                ny.neste = tmp
                tmp.forrige = ny
                self.midt = ny
        
            else: #sette til hoyre for midt og oppdatere peker til ny
                tmp = self.midt #tidligere mid peker
                tmp.forrige = ny #tidligere mi
                ny.neste = tmp.neste
                ny.forrige = tmp
                tmp.neste = ny

                self.midt = ny

        self.lengde += 1

    def get(self, i):
        current = self.start
        count = 0

        while current:
            if count == i:
                print(current.element)
            count+=1
            current = current.neste

   
     

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




 #1 1 3 2
 #0 1 3 3
      #_


#1 1 1 3 2 
#0 1 2 3 4 
    #_
