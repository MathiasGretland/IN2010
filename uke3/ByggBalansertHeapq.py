
"""
For Python kan du bruke heapq5
. De eneste operasjonene du trenger
er: heappush() og heappop(), samt kalle len() for å få størrelsen på heapen.
"""


# oppgave 4 a)

import sys
import heapq


sortertInput = []

for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    heapq.heappush(sortertInput, int(line))

# metoden printer tallet i miden av listen foer den lager nye lister med det til
# hoyere og venstre for tallet som blir printet,
# og kaller paa metoden rekursivt for de nye listene


def recPrint(que):
    if(len(que) < 1):  # returner hvis listen er tom
        return

    leftQue = []
    rightQue = []
    midIndex = int((len(que))/2)

    for i in range(len(que)):
        if i < midIndex:
            element = heapq.heappop(que)
            heapq.heappush(leftQue, element)
        elif i > midIndex:
            element = heapq.heappop(que)
            heapq.heappush(rightQue, element)

        else:
            print(heapq.heappop(que))

    recPrint(leftQue)
    recPrint(rightQue)


recPrint(sortertInput)
