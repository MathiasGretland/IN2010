"""
1.
a)
Et spenntre til en sammenhengende graf vil alltid inneholde n - 1 kanter,
Så når det er 12 noder, så vil spenntre ha 11 kanter

b) Kruskal kan finne spennskoger til en graf, det betyr at en graf ikke behøver å være sammenhengende, en spennskog er satt sammen
av flere spenntrær
Så hvis man har 6 noder, og 6 kanter, så betyr det at vi kan bruke alle 6 kantene på bare 4 av nodene, som betyr at da får vi
Et spenntre som er de 4 nodene + et spenntre som består av en node + et spenntre som består av den siste noden.
Da trenger vi kun kanter som lager et spenntre ut av de 4 nodene, og da trenger vi kun 3 kanter

så svaret er 3


c)
Minimale spenntær er spenntrær hvor man finner den billigste stien, det gjøres med
Prim
Kruskal 
Boruvka

VIKTIG! BFS og DFS finner spenntrær for uvektede grafer. Men disse er ikke minimale


f)
O(n^5)

h)
Ingen negative sykler - Bellman-Ford
Ingen negative kanter - Dijkstra
Vektet DAG - TopSort
Uvektet - BFS

i)
GATTACA

j)

32  40  17  98  59
0   1   2   3   4

"""


"""
2.
a)
1. Veiene mellom hvert rom
2. Hvor mange rom man kan komme seg til fra den noden, altså hvor mange rom man kan gå til fra det rommet man er i
3. 0, fordi som spesifisert i kravene til et skattekammer, så kan man ikke gå til noen andre rom hvis man er i et skattekammer
4. 1


c)
1. 1, fordi et skattekammer ikke kan nå noen andre rom
2. 0, fordi igjen, et skattekammer kan ikke nå noen andre rom

d) Da vil det ikke finnes noen sti som går igjennom alle nodene.

e)
1. Siden s kan nå alle rom, siden vi vet at den er et startrom, vet vi at t også kan nå alle rom, enten direkte eller via s. 
Derfor er t også et startrom
2. Igjen da så kan alle nodene i Cs nå hverandre, som betyr at hvilken som helst vilkårlig node derfra kan nå s, og siden man kan komme
seg videre fra den til alle andre noder, er de andre også nødt til å være startnoder

f)
Husk at det finnes en startkomponent som har inngrad 0, dette vil være startkomponenten.

Her kan vi få den til å kjøre SCC på grafen for oss:

Sjekker så hvilke noder som tilhører de forskjellige komponentene og deler de inn

Deretter sjekke om alle nodene i en komponentene har mer enn 0 i utgrad/inngrad, den komponenten som har det vil være startkomponenten vår

Sjekker så om den inneholder 3 noder, hvis ikke kan vi returnere false

Så går vi gjennom og ser om det finnes en komponent som har utgrad = 0, dette vil være skattekammeret vårt, 
sjekker da også om den kun inneholder 1 node, ellers returnerer vi false.

g) Den jeg snakker om her går igjennom alle komponentene to ganger så O(|SCC| + |SCC|)

h)

"""


"""
3.
f) Fordi det kun er den første halvparten av arrayet som kan ha barn, det vil da tilsi at den andre halvparten ikke har barn.
Og det er dermed ikke nødvendig å sjekke om en av barna er større, for så å måtte bytte hvis en av dem er. Når vi allerede vet at de ikke
har barn


g)
for i from n - 1 down to 0 do:
    A[0], A[i] = A[i], A[0]
    BubbleDown(A, 0, i)

h)
Procedure BubbleDown(A, i, n):
    left = 2*i + 1
    right = 2*i + 2

    j = i
    if A[left] > A[j] then:
        j = A[left]
    if A[right] > A[j] then:
        j = A[right]
    
    if j != i then:
        A[i], A[j] = A[j], A[i]
        BubbleDown[A, j, n]
    
"""