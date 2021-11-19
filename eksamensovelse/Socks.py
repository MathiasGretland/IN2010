
antallPar = input()

pile = input().split()
otherPile = []

antallMoves = 0
while pile:
    pileTop = pile[-1]
    otherTop = None
    if otherPile:
        otherTop = otherPile[-1]

    if pileTop == otherTop:
        pile.pop()
        otherPile.pop()
        antallMoves += 1
    else:
        elem = pile.pop()
        otherPile.append(elem)
        antallMoves+=1

if otherPile:
    print("impossible")
else:
    print(antallMoves)