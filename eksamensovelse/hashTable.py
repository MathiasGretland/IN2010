class Ting:
    def __init__(self, element, k):
        self.element = element  # dataen som blir lagret i noden
        self.k = k

hashTable = {0: None, 1: "xd", 2: "awd", 3: "adwa"}

print(hashTable)
t = Ting("swag", 54)

def put(e):
    teller = 0
    n = len(hashTable)
    tall = e.k % n 
    while teller != n: # Så lenge telleren ikke går over lengden til hashTabellen så kan den kjøre, går den over så betyr det at tabellen er full 
        if tall < n: #Passer på at indexen ikke går ut av tabellen slik at det blir index out of bounds
            if hashTable.get(tall) == None: #viss det er ledig plass
                hashTable[tall] = e.element
                return True
            else: #hvis det ikke er ledig plass, så skal den prøve neste plass
                tall += 1
                teller += 1
        else: #viss vi er på slutten av tabellen altså index n - 1, så skal vi starte på nytt. Altså sette index til = 0
            tall = 0
            teller += 1
    return False

def main():
    print(put(t))
    print(hashTable)


main()