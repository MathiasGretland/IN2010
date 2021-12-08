"""
1.
Den er i konstant tid O(1), men avhenger av hva som skjer i //Gjør noe. Avhengig av hva som skjer der
kan "Worst-case"-tidskompleksiteten bli verre

O(n^2)

    O(2n) = O(n)
        O(n)
O(n^2)

O(n^3)
"""

"""
2.
a) 4
b) 3
c) 28
d) nei
e) 2, hvis rota ikke telles som barn
f) 4
g) 25, 30
h) 1, og det er rota
i) RRL 38
j) 4
k) 45
l) nei
m) 38
n) 30, 40
o) 22
p) nei

"""

"""
3.
Procedure WritePathToNode(v, verdi, stringSoFar):
    if v is None then:
        return "Verdien " + verdi + " finnes ikke i treet"
    if v.v = verdi then:
        return stringSoFar + " " + verdi
    if v.v < verdi then:
        writePathToNode(v.right, verdi, stringSoFar+"R")
    else: //if v.v > verdi
        writePathToNode(v.left, verdi, stringSoFar+"L")
"""

"""
4.
Procedure removeLessThan(Node n, int value):
    if n is None then:
        return "verdien finnes ikke i treet"
    if n.v = value then:
        n.l = removeLessThan(n.l, value)
        return n
    if n.v < value then:
        return removeLessThan(n.r, value)
   
"""

"""
5.
De er noen terrorister for å bruke 11 på en eksamen uten kalkulatorm, men jaja

Vi har en hashtabell med lengde 11:


0   1   2   3   4   5   6   7   8   9   10


a)
Vi skal sette inn 12 elementer, så dette betyr at lukket hashing ikke vil fungere
siden hashtabellen kun er av lengde 11. Da vil det ikke være plass til det siste elementet,
altså 91, derfor bruker jeg åpen hashing for å løse denne.

b)
Indeks  :   [verdier]
0   :   [99, 33]
1   :   [78, 12]
2   :   [57]
3   :   [91]
4   :   []
5   :   []
6   :   [61]
7   :   [18]
8   :   [74, 19]
9   :   [42, 20]
10  :   []

"""



"""
6.
Procedure put(e):
    i = e.k % hashTable.length
    for k from 0 to hashTable.legth - 1 do:
        if hashtable[i] is None or hashTable[i] = e then:
            hashTable[i] = e
            return true
        else: //Her er det ikke ledig, gå til neste
            if i = hashTable.length - 1 then:
                i = 0
            else:
                i = i + 1
    return false //Returnerer false, hvis den har gått igjennom hele lista uten å kunne sette inn e


"""


"""
7.
Blir gitt arrayet: [,9,5,7,8,25,13,9,6]
SÅ! Heap må enten være max eller min heap, og en heap må alltid være et komplett tre.
Så at index 0 i arrayet er tomt, gjør ingenting, da starter bare roten på index 1,
men som vi ser er ikke 9 minste eller største tallet i arrayet. Noe som er et krav.
Derfor kan ikke arrayet representeres som et heap

"""


"""
8.
Må tegne treet, derfra kan man se hvilke tegn de forskjellige får:

A   0000
B   0001
C   01
D   1
E   001
"""


"""
9.
a)
E -> A -> D -> C -> B

b)
Nei, her dannes det en sykel:
C -> A -> D -> B -> C. Kan ikke ende opp i samme node to ganger.

"""

"""
10.
Procedure Dijkstra(G, s):
    Initialize Q as empty priority queue
    Initialize D as empty map
    for each vertex u in G do:
        D[u] = infinity
        Q.add(u, D[u])
    D[s] = 0

    while Q is not empty:
            v = removeMin()
            for each edge (v, w) in G do:
                if D[v] + w((v,w)) < D[w] then:
                    D[w] = D[v] + w((v,w))
                    change value of w in Q to D[w]

    return D

Liste over når de ble kjent: A,B,C,G,D,E,F,H
Node    Avstand Sti
XA       0       -      
XB       2       A
XC       5       A
XD       10      B
XE       24/13    D
XF       20/13      A/G
XG       9       C
XH       21/17/14     G,E,F


b) Nei, fordi si at vi starter i node B og skal til E, da vil dijkstra sin algoritme si at
det er lurere å gå til E mellom kanten som har vekt 1, og da vil det koste 1 totalt.
Men det vi ikke vet er at hvis vi tar kanten mellom B og D, og deretter D til E, vil vi få
en kostnad på: -3, som da igjen vil være kortere, men dette ville ikke algoritmen kommet fram til.
Og derfor vil ikke dijkstra finne kortest vei for denne grafen.
"""

"""
11.


"""


"""
12.
Her kan vi bruke Topologisk sortering for å gå igjennom å finne avhengigheter av hverandre

Procedure TopologiskSortering(G):
    Initialize S as empty stack
    Initialize D as empty map
    for each vertex u in G do:
        inCount(v) = degin() //Finner innverdien til alle nodene
        if inCount(v) = 0 then:
            S.add(v)
    i = 1
    while S is not empty:
        v = S.pop()
        D[v] = i
        i = i + 1
        for each edge(v,w) in G do:
            inCount(w) = inCount(w) - 1
            if inCount(w) = 0 then:
                S.add(w)
    
    if i > n then:
        return D
    return "G has a cycle"

Procedure numberOfSemesters(G, N):
    D = TopologiskSortering(G) //Her trenger vi ikke å returnere om den har en sykel eller ikke, fordi det spiller ingen rolle, så vår metode over vil alltid returnere D
    n = D.size()
    AntallSemestere = 0
    for i from 0 to n - 1 do: //Siden vi skal ta N emner, altså vi må ta alle, kan vi bare dele de opp slik:
        emner = 0
        if emner < 3 then:
            emner = emner + 1
        if emner = 3 then:
            antallSemestere = antallSemestere + 1
            emner = 0
    
    return AntallSemestere
"""


"""
14.
Her ville jeg brukt bucket sort, fordi her kan vi putte hver karakter inn i en bøtte.
Og dermed putte hver elev inn i den bøtten som tilhører karakteren sin. Står også at vi skal
sortere fra best til dårligst, så når vi har sortert den ferdig, er vi nødt til å reversere bøtten
Bucket sort blir også brukt fordi den har worst-case på O(N + n) tid, som da vil være veldig raskt
for denne type oppgave

Procedure BucketSort(A):
    La B være en array med N antall lister
    for i from 0 to n - 1 do:
        La k være assosiert med A[i]
        Legg A[i] til på slutten av B[k]
    j = 0
    for k from N - 1 down to 0 do:
        for hver x fra listen B[k] do:
            A[j] = x
            j = j + 1
        end
    end

    for i from 6 down to 1 do:
        for each elev x in B[i] do:
            fjern x fra B[i] og legg til på slutten av output array (elever)



Procedure RadixSort(A)
    d = lengden på det største sifferet
    for i from d to 0 do:
        A = BucketSort(A) på det ite sifferet
    
    return A
"""