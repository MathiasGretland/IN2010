
# oppgave 4 a)

import sys

sortertInput = []

for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    sortertInput.append(int(line))

# metoden printer tallet i midten av listen foer den lager nye lister med det til
# hoyre og venstre for tallet som blir printet,
# og kaller paa metoden rekursivt for de nye listene


def recPrint(liste):
    if(len(liste) < 1):  # returner hvis listen er tom
        return

    i = int((len(liste) - 1) / 2)

    midElement = liste[i]
    leftArray = liste[0:i]
    rightArray = liste[i+1:len(liste)]

    print(midElement)
    recPrint(leftArray)
    recPrint(rightArray)


recPrint(sortertInput)
