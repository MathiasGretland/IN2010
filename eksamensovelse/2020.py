"""
Hva er en algoritme? En sekvens av steg for å oppnå et resultat, gjerne også kalt en oppskrift for å finne en løsning

Hva er en datastruktur? En beholder av data i en strukturert form
"""


"""
Binære søketrær
a) c, fordi hver foreldrenode kan kun ha to barn
b) 5, fordi roten er 4, venstre barnet til 4 er 2, som er greit fordi 2 < 4, venstrebarnet til 2 er 5, noe som ikke er greit fordi 2 < 5,
samtidig som også at 2 < 4 < 5
c) nei, binære søketrær har ingen grense på max høyde slik som AVL Trær
d) ja, hvert AVL tre kan også representeres som et binært søketre
"""

"""
Grafegenskaper
    - ingenting fordi den allerede er sammenhengende
    - fjerne kanter
    - fjerne kanter
    - ingenting fordi G er ikke et tre
    - Ingenting fordi den er en DAG
    - Legge til kanter
    - Den er ikke sterkt sammenhengende, legg til kanter, viktig! En rettet graf er sterkt sammenhengende dersom det går en (rettet) sti
     fra enhver node til enhver annen node. (Både u→v og v→u.)
    - Nei, H er ikke sterkt sammenhengende
    
"""

"""
Linear Probing (Lukket hashing)
Tomt array på størrelse 10
blir altså:

29          93  74  13  45     48  99
0   1   2   3   4   5   6   7   8   9

Kan bli representert slik da:
29  0   0   93  74  13  45  0  48  99 //Skriver 0, fordi husk at dette er et array, antar at vi også kan skrive NULL eller None
0   1   2   3   4   5   6   7   8   9

Skal putte inn 7 elementer så dette går fint
Hashfunkjsonen er k mod N, altså k % 10
Her spoiler den at hasher er tall sitt siste siffer, som er sant fordi det blir basically bare å dele på 10 helt til det ikke går og ta resten

93 = 3
48 = 8
74 = 4
99 = 9
29 = 9
13 = 3
45 = 5
"""

"""
Søk

Viktig å notere seg her at ingen av arrayene A og B er sortert, men at du skal gå igjennom hvert element i array B, og se om de finnes i array A

Intersection1 - Denne gjør bare et standard søk som skjer i lineær tid, altså O(n) noe som går helt fint, 
Bare viktig å huske at denne kan bli utrolig treig hvis den har mange elementer

Intersection2 - Denne vil feile noen ganger, fordi når man gjør et binærsøk så skal man gjøre søket på en sortert liste, 
noe som de ikke er. Derfor vil ikke denne være optimal å bruke noen av gangene

Intersection3 - Denne gjør en heapsort av array A før den bruker vanlig binæsøk, noe som vil være optimalt
Binærsøk vet vi er i O(log(n)) tid, men siden den må utføre en heapsort først som har worst case O(n log(n)), kjører den på worst case
O(n log(n)), som vil være raskt hvis størrelsen på input blir stort. 

Intersection4 - gjør også heapsort, men den gjør det for hvert element, noe som er totalt unødvendig, og vil ta veldig lang tid.
Denne er basically ubrukelig når vi har intersection3

Basert på denne analysen vet vi at vi kun trenger å bry oss om intersection 1 og 3

--------------------------------------------------------------------------------------------
Hvis B inneholder ett element, altså k = 1?

Hvis det kun er 1 element vi skal sjekke er det litt overfladisk å utføre en heapsort først, som betyr at intersection1
hvor vi rett fram sjekker om kun det ene elementet finnes, vil være raskt, da denne utfører færre operasjoner
Svar: Intersection 1


Hvis B inneholder log(n) elementer, altså k = log(n)?

Denne er tricky å tenke seg fram til, men vit at hvis man bruker log(n) så vil ikke kjøretiden øke så mye uansett, hvor mange
fler elementer vi putter på, derfor er det vilkårlig å si at begge er raske, da vi antar at log(n) ikke blir altfor stort
Svar: Intersection1 og Intersection3

Hvis B inneholder n elementer, altså k = n?

VIKTIG! husk at k = størrelsen til B, og n = størrelsen til A, dette betyr at for intersection1 som har kompleksiteten O(n),
vil kjøre O(n * n), som basically tilsier O(n^2)
Mens intersection3 vil kjøre på O(n log(n) * n), den vil dermed bare være en konstant, og det blir fortsatt O(n log(n))
Svar: Intersection3

Hvis B inneholder n^2 elementer, altså k = n^2? 
Blir ish lik tankegang som over, litt usikker her om O(n * n^2) bare fjerner konstanter og blir O(n^2), men da ville ikke
løsningforslaget gitt mening så det blir O(n^3), confirmed av Jakob
og dermed blir Intersection3 raskere fordi O(n log(n) * n^2) tilsier O(n^2 * log(n))
Svar: Intersection3
"""

"""
AVL her må man se på tegning for hånd, men skriver fortsatt svarene her
VIKTIG! Husk at dette er opprinnelig et binært søketre, hvor det blir gjort en AVL-innsetting, til slutt, denne gjør at det binære søketreet
blir gjort om til et AVL tre, fordi etter innsetting så vil det bli gjort rotasjoner
a)  Se bilde

b) 4

c) Ja

d) 2
"""

"""
Subanagram

Streng S, og subanagram W

a) 
O(n) worst case her er O(n)
men husk at her må du se hva som skjer inne i metoden, siden den påpeker at w angir størrelsen av W, og s angir størrelsen på S
for c in S do: altså O(s)
    inne i loopen skjer:
    if c is in r then: betyr basically: if c is in W then: som betyr at du går igjennom den også, O(w)
Som da tilslutt tilsier:
O(w * s)

b) 
Procedure IsSubanagramOf2(W,S):
    F = FreqTable(W)
    R = FreqTable(S)

    for each char c in W do:
        if F.get(c) > R.get(c):
            return False
    return True

c) er drøftingsoppgave

d)
Procedure SortSubanagrams(A)
    La B være et array med N tomme lister
    n = A.length
    for i from 0 to n - 1 do;
        La k være nøkkelen assosiert med B[i]
        Legg til A[i] på slutten av listen B[k]
    j = 0
    for k from 0 to N - 1 do:
        for hver x i listen B[k] do:
            A[j] = x
            j = j + 1
        end
    end
"""

"""
Fire typer grafer

Type 1  
Type 2, Bellman-Ford
Type 3, BFS?
Type 4, Sammenhengende komponenter?
a)
Procedure Type2Verifier(G,C):
    


b)

c) Det er fordi 2-sammenhengende betyr det samme som bikonnektiv, altså at hvis man fjerner en node i en sammenhengende graf.
Og grafen fortsatt er sammenhengende, da vil den være 2-sammenhengende, det er først hvis man fjerner 2 noder fra grafen, den ikke blir sammenhengende
, men siden vi fortsatt kan sykle rundt i byen etter et hus er stengt ned, betyr det at den er bikonnektiv.


d)
Procedure TwoPaths(G, C, s, t):
    Her kan man teknisk sett finne en sti, også reversere den stien, for å finne en annen
    
"""



"""
HTML

a)
Procedure GoodDivs(A):
    i = 0
    for tag c in A do:
        if c = "<div>" then:
            i = i + 1
        else:
            i = i - 1
    if i < 0 then:
        return False
    return True

b)
Procedure GoodTags(A):
    for tag c from 0 to n - 1 do:
        if isOpen(c) is True:
            for tag k from c to n - 1 do:
                if TagType(k) = TagType(c) and isOpen(k) is False:
                    continue
                return False
    return True
"""