from collections import defaultdict, deque
from heapq import heappush, heappop

def buildgraph(lines):
    V = set()
    E = defaultdict(set)
    w = dict()

    for line in lines:
        v, u, weight = line.strip().split()

        V.add(v)
        V.add(u)

        E[v].add(u)
        E[u].add(v)

        w[(v, u)] = int(weight)
        w[(u, v)] = int(weight)

    return V, E, w

def dfs_rec(G, s, visited, result): #Bry deg om denne metoden
    _, E, _ = G
    result.append(s)
    visited.add(s)
    for v in E[s]:
        if v not in visited:
            dfs_rec(G, v, visited, result)
    return result

"""
Pseudokode av DFS
--------------------------------
Input: En graf G, og en start node s
Output: Alle noder som kan nås fra s
Procedure DFS(G, s)
    visited(s) = true
    for each edge (s, v) in G do:
        if visited(v) = false then:
            DFS(G, v)
    end


Kjøretid:
O(|V| + |E|) = altså: alle nodene + alle kantene
"""
def dfs(G, s): #Ikke bry deg om denne metoden!
    _, E, _ = G
    visited = set()
    stack = [s]
    result = []
    
    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        result.add(v)
        for u in E[v]:
            stack.append(u)
    return result


def bfs(G, s):
    _, E, _ = G
    visited = set([s])
    queue = deque([s])
    result = []

    while queue:
        v = deque.popleft(queue)
        result.append(v)
        for u in E[v]:
            if u not in visited:
                visited.add(u)
                queue.append(u)
    return result


"""
Pseudokode av BFS
--------------------------------
Input: En graf G, og en start node s
Output: Alle noder som kan nås fra s
Procedure BFS(G, s):
    visited(s) = true
    deque.append(s) #legger til på slutten
    while deque not empty:
        v = deque.popleft() #tar første elementet
        for each edge(v, w) in G do:
            if visited(w) = false then:
                visited(w) = true
                deque.append(w)
            end
        end
    end

Kjøretid:
O(|V| + |E|) = altså: alle nodene + alle kantene
"""

"""
Dette er de to algoritmene som går igjennom en SAMMENHENGENDE graf. Det betyr at det finnes en sti mellom alle par av noder i V.
Når en graf er sammenhengende, så er det tilstrekkelig å starte med en vilkårlig node u I V, og besøke u sine naboer, 
og deres naboer sine naboer, og så videre, og da til slutt ha besøkt alle noder i V.

# DFS: Gå så dypt som mulig inn i grafen som mulig, det vil si at du følger (ikke-besøkte) naboer så langt du kan;
# BFS: Besøke alle direkte naboer før du besøker naboer sine naboer

VIKTIG! BFS finner korteste stier for sammenhengende grafer som er uvektede, det gjør ikke DFS!!!!!
Men her er vi nødt til å mappe foreldrene til de ulike nodene, og basert på det så kan vi se at det danner et tre.
Som igjen gjør at vi kan lese ut den korteste stien fra s til alle andre noder
"""


"""
Topologisk sortering! En graf kan beskrive avhengigheter mellom ting, f.eks. temporale avhengigheter
rettede, asykliske grafer (directed acyclic graphs, DAG)
kan være nyttig å kunne ordne nodene etter avhengighetene

Ideen:
    - Fjern alle noder som ikke har avhengigheter, slik vil det oppstå noder som igjen ikke har avhengigheter, helt til det er ingen igjen.
    - Dette vil da lage en rekkefølge, som forklarer hva vi er nødt til å gjøre før vi kan gjøre noe annet, se morgenrutine eksempelet fra videoen.

"""

"""
Pseudokode av Topologisk sortering
--------------------------------
Input: En graf G med n noder
Output: En topologisk ordning av nodene i G, eller G har en sykel
Procedure TopologiskSortering(G):
    Initialize S as empty Stack
    for each vertex v in G do: //Sjekker for alle nodene i grafen om de har noen avhengigheter eller ikke
        inCount(v) = degin(V) //Denne er litt yikes, men den ser på hvor mange avhengigheter noden har. !!! inCount betyr hvor mange kanter den har som peker mot seg!
        if inCount(v) = 0 then: //Hvis noden ikke har noen avhengigheter, så skal den pushes på stacken
            S.push(v)
    i = 1
    while S not empty do:
        v = S.pop() //Tar ut elementet i stacken
        output[i] = v //Angir hvilken rekkefølge vi skal utføre handlingene i
        i = i + 1  //Dette gjør jo at alle får forskjellig tall, som tilsier hvilken rekkefølge de skal gjøre ting i, f.eks. 1 = dusje, 2 = undertøy, 3 = bukse. osv...
        for each edge (v, w) in G do: //Her går vi da videre fra vår node, gjennom en kant, til en ny node w
            inCount(w) = inCount(w)-1 //Og siden de andre nodene nå er "fjernet" så vil jo barna til de forrige nodene uten avhengigheter, være de som ikke har avhengigheter
            if inCount(w) = 0 then: //Dette vil jo da gjøre helt til det ikke finnes noen noder igjen, fordi så lenge det finnes noder uten avhengigheter, så vil det alltid være noder på stacken
                S.push(w)
    if i > n then: //Hvis i har et større tall en antall noder i grafen, så vil vi ha en sykel.
        return output
    return "G has a cycle"

Hvorfor finner den sykler?
i blir inkrementert hver gang noe blir poppet fra S
En node kommer på stacken når alle sine forgjengere har blitt fjernet fra stacken
Hvis i <= n og S er tom, er det noder som er avhengig av hverandre, som betyr at det er en sykel.



Kjøretid:
O(|V| + |E|) = altså: alle nodene + alle kantene
"""








"""
------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""




"""
Korteste stier for vektede grafer, Betyr Dijkstra algoritmen
Vi vet at DFS bruker en stack (eller gjøres rekursivt slik som over), og BFS bruker en FIFO-kø, altså en deque (setter inn på slutten, tar fra foran). 
Mens Dijkstra bruker heller en prioritetskø. En prioritetskø trenger en total ordning over elementene som legges på køen, altså en sorteringskriterie
#USIKKER! Tror dijkstra kun fungerer på RETTEDE vektede grafer. Sike fungerer på urettede også.

Prioritetskøen skal holde noder som elementer, og bruke en "estimert avstand" D til sammenligning.
D skal inneholde den korteste veien vi har funnet så langt
s får D[s] = 0
Hver gang vi fjerner et element u fra prioritetskøen, ser vi på naboene v til u og ser om vi har funnet en kortere vei til v, oppdaterer evt. D[v].

En prioritetskø definerer vi som en heap, altså den med lavest/minst verdi, er da av høyest prioritet, og vil derfor være neste man ut, når man pop'er på heapen
"""

def dijkstra(G, s):
    V, E, W = G
    Q = [(0, s)] #Dette vil jo da tilsi at startnoden har verdi 0 på stacken, siden vi må starte et sted
    D = defaultdict(lambda: float('inf')) #Altså hvis noden som blir lagt inn ikke har noen verdi enda, så får den bare 'inf', short for infinity, altså så høyt som mulig.
    D[s] = 0 #Den første noden vil koste 0 å komme til, fordi det er der vi starter, og vi må derfor legge den inn først slik

    while Q: #Så lenge heapen/prioritetskøen ikke er tom, så kjører vi på
        cost, v = heappop(Q) #Tar av en node, med dens vekt av heapen
        for u in E[v]: #For hver kant
            c = cost + W[(v, u)] #Tar kostnaden for å komme seg til den noden vi er i nå (cost) + kanten mellom der vi er nå, og der vi skal til (W[(v, u)]), eks: 6 + 5 = 11
            if c < D[u]: #Hvis det koster mindre å komme seg dit med den veien vi går igjennom nå, enn den som er der fra før, så har vi funnet en kortere vei,
                D[u] = c #Oppdaterer noden slik at den får riktig kostnad
                heappush(Q, (c, u)) #Legger den nye noden, med oppdatert cost på stacken fordi da må den gås igjennom
    
    return D

"""
Pseudokode av Dijkstra
--------------------------------
Input: En graf G og en start node s
Output: Korteste stier til hver enkelt node fra s
Procedure Dijkstra(G, s):
    Initialize Q as empty heap
    Initialize D as empty map
    for each vertex u in G do:
        D[u] = infinty #altså evig stort
        Q.add(u, D[u])
    D[s] = 0 #Startnoden får kostnad 0, fordi det er der vi starter

    while Q not empty:
        v = Q.removeMin() #Fjerner det minste elementet
        for each edge (v, t) in G do:
            if D[v] + W(v,t) < D[t] then: #Hvis det koster mindre å komme seg dit med den veien vi går igjennom nå, enn den som er der fra før, så har vi funnet en kortere vei,
                D[t] = D[v] + W(v,t)
                change value of t in Q to D[t]
            end
        end
    end


Kjøretid:
O(|E| log(|V|)) som tilsier O(n log(n))
"""
"""
VIKTIG TIL DIJKSTRA! Grådig fungerer ikke alltid, med negative kanter må vi besøke den samme noden og revurdere avstanden flere ganger!
Dette vil ikke fungere i praksis, og vi bruker derfor Bellman-Ford istedenfor
"""


"""
Bellman-Ford algoritmen! Finner korteste stier i grafer med negative kanter. Hvis grafen inneholder en negativ sykel (der summen av vektene er negativ), finnes det ingen kortest sti i den
Bellman Ford finner kortest sti, eller oppdager negative sykler ved noen smarte triks. 
VIKTIG! Husk at hvis en graf har en negativ sykel, så betyr det at den kan gå rundt i det uendelige og alltid finne en kortere vei, men i praksis så blir jo ikke det riktig.

Ideen:
    - Den lengste stien som ikke er en sykel inneholer |V| - 1 kanter. 
    - Her bruker vi ikke en prioritetskø, oppdaterer heller estimert avstand D for alle noder |V| -1 ganger.
    - Hvis det finnes en node hvor estimert avstand fortsatt blir mindre etter det, inneholder G en negativ sykel.
"""

"""
Pseudokode av Bellman-Ford
--------------------------------
Input: En graf G og en start node s
Output: Korteste stier til hver enkelt node fra s
Procedure Dijkstra(G, s):
    Initialize D as empty map
    for each vertex u in G do:
        D[u] = infinity #altså uendlig
    D[s] = 0 //Dette er start noden vår
    for i from 1 to |V| - 1 do:
        for edge (u, v) in G do:
            if D[u] + w((u,v)) < D[v] then:
                D[v] = D[u] + w(u, v)
    for edge (u, v) in G do: //Her sjekker den om den klarer å finne et bedre estimat, altså at hvis den går en videre, og stien koster mindre, har vi en negativ sykel
        if D[u] + w((u, v)) < D[v] then
            return "G has a negative cycle"
    
    return D


Kjøretid:
O(|E| * |V|) som tilsier O(n^2)
"""




"""
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""




"""
Minimale spenntrær! Ordet er veldig beskrivende: Vi ønsker et tre som spenner en graf G = (V, E), altså et tre som kobler alle nodene i V,
og kun bruker kantene fra E. 
Det vi skal se på nå er å finne et MINIMALT spenntre, altså et tre der den totale vekten av kantene er minimert. 
Vi skal kun løse dette problemet for urettede og vektede grafer (i motsetning fra BFS, DFS og Dijkstra, som fungerer like godt på rettede grafer) 
som vi antar er sammenhengende.

Altså! alle alogritmene tar en vektet, sammenhengende graf G og returnerer et minimalt spenntre T.

Algoritmene for minimale spenntre er:
VIKTIG! Alle har samme verste tilfellet analyse... så hvilken algoritme skal man velge?
Prims algoritme (grådig valg av noder)
Kruskals algoritme (grådig valg av kanter) -- På tynne grafer er Kruskal i praksis ofte raskere, Hvis man har tilgang til kantene sortert etter vekt: Kruskal raskere
Boruvkas algoritme (grådig valg av kanter, parallelliserbar) -- Er lett å parallellisere
"""


"""
Starter med Prim. Viktig å påpeke at det ikke har noe å si hvilken node vi starter på, siden alle skal være med til slutt,
Her starter man på en node, og velger den kanten som er billigst til en ny node. 
eks.: node "F" har kantene ((F, D), 3) og ((F, E), 2). Her velger vi naturligvis ((F, E), 2), da den er den billigste kanten, med vekt 2
Da har vi dannet et lite tre, som består av (F, E), da må vi se hvilke kanter som kan fører til en ny node som ikke er med i treet vårt, og dermed velge den billigste
VIKTIG KRITERIUM! Man legger aldri til kanter som danner sykler! Her er det altså viktig å holde styr på hvilke noder vi allerede har besøkt,
slik at de ikke blir lagt til mer enn 1 gang
Dette gjør vi helt til vi har fått med alle nodene fra den sammenhengende grafen G, inn i vårt minimale spenntre T.

Prim implementasjonen ligner veldig på Dijkstra, både i Python kode og i pseudokode
"""

def prim(G):
    V, E, w = G
    s = next(iter(V))
    Q = [(0, s, None)] #Dette er at startnoden har vekt 0, og peker til ingen. Q er da en heap, altså en prioritetskø
    parents = dict()

    while Q:
        _, v, p = heappop(Q)
        if v in parents: #Hvis noden allerede finnes i parents, gå til neste node i stacken
            continue
        parents[v] = p #Hvis noden ikke finnes i parents, så skal den legges til og peke på den noden med lavest kant mellom seg. Altså den referer til en kant

        for u in E[v]: #For hver node som node v peker til, legg den til i stacken med vekten sin. Vekten er viktig for å holde rekkefølgen i prioritetskøen, slik at det alltid blir den korteste kanten
            heappush(Q, (w[(v, u)], u, v))
    
    return parents


"""
Pseudokode av Prim
--------------------------------
Input: En sammenhengende graf G 
Output: Et minimalt spenntre T 
Procedure Prim(G):
    Initialize T as empty tree
    Initialize Q as empty heap 
    Initialize D as empty map //Denne holder på kostnader
    for each vertex u in G do:
        D[u] = infinity #altså evig stort 
        //Q contains (Node, edge), where Edge has lowest weight of edges from T to Node, and uses D[u] to compare
        Q.add(((u, None), D[u]))
    pick v in V //henter ut en startnode, dette kan være hvilken som helst node fra grafen 
    set D[v] = 0
    while Q not empty do:
        (s, e) = Q.removeMin()
        add s and e to T
        //check neighbors of s in Q
        for edge a = (s, z) with z in Q do: //Går igjennom naboene til s, altså kantene mellom s og andre noder
            if w(a) < D[z] then: //Hvis vekten til den kanten er mindre enn den som allerede allerede er på heapen så skal den byttes
                D[z] = w(a)
                change entry of z in Q to ((z,a), D[z]) //Endrer hvilken vei vi skal komme til den nye noden på heapen fordi vi har funnet en enklere vei
            end
        end
    end
    return T


Kjøretid:
O(|E| log(|V|)) som tilsier O(n log(n))
"""


"""
VIKTIG PÅPEKNING OM O NOTASJON I HEAPS! en heap-insert, altså hvor man legger til på heapen, vil alltid være logaritmisk tid på størrelsen av heapen
I da Prims algoritme, skjer dette i starten og vil derfor være O(log(|V|))

Samme gjelder for heap-remove, vil alltid være logaritmisk tid på størreslen av heapen, altså O(log(|V|))
"""


"""
Neste ut er Kruskals algoritmen, imotsenting til prim så velger vi ikke ut noder, men velger alltid den billigste kanten. 
Altså ser hvilke noder som er på hver ende av den kanten f.eks.: kanten med vekt 1 ('B', 'D') gir da nodene B og D med i spenntreet, kanten med vekt 2 ('E', 'F') gir da nodene E og F osv...
VIKTIG! Skal sies at et spenntre ikke alltid er unikt, det kan ha flere spenntrær, men fra eksempelet på forelesning så hadde det ikke det.

"""


"""
Pseudokode av Kruskal
------------------------------------------------------------------------
Input: En sammenhengends graf G
Output: Et minimalt spenntre T
Procedure Kruskal(G):
    initialize T as empty tree
    initialize empty Q for edges //En tom heap
    for each vertex v in G do:
        define C(v) = {v} //Lager en cluster, starter da med å si at hver node er clustered til seg selv
    while T has fewer than n - 1 edges do: //Et minimalt spenntre har alltid en mindre kant enn det finnes noder i treet. 
        (u, v) = Q.removeMin() //Tar ut den billigste kanten i vår heap
        if C(u) is not C(v) then: //Altså hvis ikke den forbinder to clusters som allerede er sammenhengende, så legger vi den til i treet, og merger clusterne våre
            add (u,v) to T
            C(u), c(v) = C(u) union C(v)
        end 
    end
    return T

//VIKTIG! Dette betyr at den alltid velger den billigste kanten mellom to noder, som da danner et cluster, den vil dermed slå sammen clusters,
Så lenge det ikke allerede finnes et cluster som gjør den sammenhengende. Dette gjør at den vil holde på helt til alle nodene er slått sammen
fordi, når while-loopen tar slutt så vil det bestå av et minimalt spenntre, hvor kantene har vært de som bestemmer hvem som skal med eller ikke

Kjøretid:
O(|E| log(|V|)) som tilsier O(n log(n))
"""

"""
VIKTIG PÅPEKNING OM CLUSTER-MERGE! Hver cluster-merge dobler størrelsen av clusteret/halverer antall clustere, helt til det kun finnes et cluster, som da teknisk sett vil utgjøre treet vårt. 
Dermed: Hver node merged inn i ny cluster log(|V|) ganger. Summert blir dette: O(|V| log(|V|))
"""

"""
Siste ut er Boruvkas algortimen, den operer litt lik som kruskals, men er bedre egnet til parallellisering. Her sier vi at hver node blir sin egen komponent.
Så tar den for hver komponent og ser hvilken kant som er den billigste kanten ut fra den komponenten og markerer den.
Disse kanten utgjør da en sammenslåing av komponenter, slik at alle komponenter med en kant til hverandre som er blitt markert, er nå en komponent.
Og slik repeteres det, ser på hver komponent og ser hviklen kant som er billigst utfra den komponenten til en annen. Dette gjør man helt til man står igjen med en stor komponent
Når vi da har slått sammen alle komponentene, så vil vi se at de kantene som vi har markert, danner et minimalt spenntre
"""

"""
Pseudokode av Boruvkas
------------------------------------------------------------------------
Input: En sammenhengends graf G
Output: Et minimalt spenntre T
Procedure Boruvkas(G):
    initialize T as empty tree
    for each vertex v in G do: //Legger til hver node i treet, disse kommer til å være våre komponenter
        add v to T
    while T has more than one component do:
        for each component C in T do:
            for each vertex v in C do: 
                Comp(v) = C
            cheapest(C) = None //cheapest representeres som den billigste kanten som går utfra komponenten, denne vil da overskrides
        for each edge e = (u, v) in G do: //For hver kant i G
            if Comp(u) is not Comp(v) //Sjekker om dette er en kant som forbinder to komponenter, dette ser vi ved å sjekke om den ene noden er i en komponent, og om den andre noden er i en komponent
                if w(e) < w(cheapest(Comp(u))) then: //Hvis den kanten er den billigste kanten mellom de to komponetene så settes den til cheapest
                    cheapest(Comp(u)) = e
                if w(e) < W(cheapest(Comp(v))) then: //Må gjøres for begge slik at det dannes en kant mellom de to komponentene
                    cheapest(Comp(v)) = e
        for each cheapest(C) that is not None do: //Hvis det finnes noen billigere kanter, så legger vi dem til i treet
            add cheapest(C) to T
    return T

Kjøretid:
O(|E| log(|V|)) som tilsier O(n log(n))
"""

"""
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""



"""
Bikonnektivitet! Det vi har sett på tidligere nå, er en graf som har vært sammenhengende, altså det finnes en sti mellom alle par av noder i G. 
I mange anvendelser så ønsker man ikke bare at grafen skal være sammenhengende, men også at den skal være bikonnektiv. Det betyr at hvis hvilken som helst node i grafen,
altså: v in V. Fjernes fra grafen, så vil grafen fremdeles være sammenhengende.
Mer generelt så sier vi at en graf er k-sammenhengende, så hvis grafen forblir sammenhengende hvis man fjerner færre en k noder. 
At en graf er bikonnektiv betyr det samme som at den er 2-sammenhengende.

Her bør man sjekke ut notatet for mer in-depth forståelse
"""

"""
Vi må først sjekke om en graf er sammenhengende og det kan vi enkelt gjøre med pseudokode, fordi her trenger vi bare å kjøre DFS eller BFS søk. Hvis man da finner en sti
som går fra en node, til alle andre noder, så har vi en sammenhengende graf. 
Metode for å sjekke dette kan for eksempel være:

Input: En graf G
Output: True eller False basert på om grafen er sammenhengende eller ikke
Procedure checkSammenhengende(G)
    v in V //Ta hvilken som helst node fra grafen.
    sti <- DFS(G, v) //Kjører DFS søk på grafen G, med noden v som startnode
    for each vertex u in V do:
        if sti.contains(u) then: //Hvis stien inneholder node u, så fortsetter vi. 
            continue
        return False //Hvis ikke stien inneholder noden, så returner vi false
    return True

Kompleksitet:
Hvis grafen ikke er sammenhengende, altså vårt worst case. Vil bli O(|V| + |E|)
Dette vil det bli uavhengig om vi bruker BFS eller DFS, fordi begge har worst case på O(|V| + |E|)
"""


"""
Så sjekker vi om en graf er k-sammenhengende.
En sammenghengende graf G er k-sammenhengende, eller k-node-sammenhengende, hvis G forblir sammenhengende om færre enn k noder blir fjernet.

Bikonnektivitet handler om 2-sammenhengende grafer (der ordet BI kommer in = 2).
En graf G er 2-sammenhengende/biconnected, hvis G forblir sammenhengende ved fjerning av en vilkårlig node
Formulert på en annen måte: hvis alle par av noder u og v har to distinkte stier (deler ingen kanter eller noder) mellom dem
MED ANDRE ORD! Det er en sammenhengende graf hvor uansett hvilken node du fjerner så vil den forsatt være sammenhengende, det er først når det fjernes 2 noder
den ikke er sammenhengende lenger
Nodene som ved fjerning føret til at grafen blir ikke-sammenhengende heter separasjonsnoder.

Dermed: Hvordan sjekke om en graf inneholder separasjonsnoder?
Vi bruker hopcroft-Tarjan algoritmen, som basically er en DFS søk, hvor man oppdaterer indeks og low nummeret til hver node underveis.
"""


"""
Input: En graf G, en startnode u, og dybden depth
Output: Alle separasjonsnoder i inputgrafen G 
Procedure HopcroftTarjan(G, u, depth):
    visited[u] = true
    low[u] = index[u] = depth
    childCount = 0
    for each edge {u,v} in G do:
        if visited[v] = false then:
            childCount = childCount + 1
            HopcroftTarjan(G, v, depth+1)
            low[u] = min(low[u], low[v])
            if index[u] != 1 then: //Sier bascially at hvis u ikke er rotnoden vår.
                if index[u] <= low[v] then: //Sjekker om indexen er mindre eller lik en etterfølger, hvis den er det, så er det en rotnode
                    sep_vertices.add(u)
        else: //Denne sier at vi har en back-edge, og hver gang vi har en back-edge, så må vi fortsatt sjekke om low nummeret vårt stemmer, for hvis neste index er lavere enn det lownummeret vi hadde før, så må vi oppdatere
            low[u] = min(low[u], index[v])
    if index[u] = 1 then: //Denne sjekker bare om roten er en seperasjonsnode eller ikke
        if childCount > 1 then: //Hvis rotnoden har flere enn 1 barn, så vil den alltid være en separasjonsnode.
            sep_vertices.add(u)
    return sep_vertices


Vi får at low[u] er det minste av (1) index[u], (2) low-nummeret til alle sine barn, og alle nodene u kan nå via en back-edge

Kompleksitet:

"""


"""
-------------------------------------------------------------------------------------------------------------------------------------------------------------
"""


"""
Sterkt sammenhengende komponenter! 
Først gå over hva en sterk sammenhengende graf er, En rettet graf er sterkt sammenhengende hvis det finnes en sti mellom alle par av noder.
Hver RETTET graf kan deles opp i sine såkalte stekt sammenhengende komponenter.

Vi krever at de sterkt sammenhengende komponentene er maksimale. Det vil si at komponenten ikke forblir sterkt sammenhengende hvis vi tar med enda en node eller kant.
Hvorfor gjør vi dette?
Vi kan også lage en graf der de sterkt sammenhengende komponentene er noder, med kanter mellom komponenter som kan nå hverande.
En slik graf vil være en rettet asyklisk graf (DAG).

For å finne de sterkt sammenhengende komponentene til G skal vi igjen bruke DFS. 

ide:
    - Sterkt sammenhengende komponentene til G forblir uendret hvis vi reverserer alle kantene.

Se videoen her, ingen pseudokode, men er tankegangen som gjelder.
"""


"""
Note til imorgen!
Se på bellman-Ford algoritmen! Den funker på rettete grafer, finner kortest sti eller oppdager negative sykler ved noen smarte triks
"""




def main():
    lines = open("eksamensovelse/linjer.txt", "r")
    G = buildgraph(lines)
    #print(dfs_rec(G, "A", set(), []))
    #print(dfs(G, "A")) XXXXX
    #print(bfs(G, "A"))
    #D = dijkstra(G, 'A')
    #print(list(zip(*sorted(D.items()))))
    #print(prim(G))

if __name__== "__main__":
    main()