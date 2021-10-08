from collections import defaultdict
from heapq import heappush, heappop
from collections import deque
from typing import DefaultDict
import csv

def buildgraph():

    V = set()
    E = defaultdict(set)
    w = defaultdict(list)

    # Kant skal bestå av to skuespillere som er bundet til en film
    # ActorToMovies er hashmap hvor "id-name" er nøkkel og "filmene" er verdier,
    # idToName er også hashmap hvor "id-name" er nøkkel og "navnet" er skuespillernavnet
    actorToMovies, idToName = readFromFileActors()

    movieIdToName, movieRating = readFromFileMovies()

    movieActors = defaultdict(list)

    # Går igjennom alle skuespillere knyttet til en gitt film
    for actor in actorToMovies.keys():
        V.add(actor)
        # Går igjennom alle filmer som en gitt skuespiller finnes i
        for movie in actorToMovies[actor]:
            if not movie in movieRating:
                continue
            if movieActors[movie]:
                for otherActor in movieActors[movie]:
                    E[actor].add(otherActor)
                    E[otherActor].add(actor)
                    
                    w[(actor, otherActor)].append(
                        (float(movieRating[movie]), movie)
                    )
                    w[(otherActor, actor)].append(
                        (float(movieRating[movie]), movie)
                    )

            movieActors[movie].append(actor)  # legge til skuspiller til film

    return V, E, w, idToName, movieIdToName, movieRating


def antallNoder(G):
    V, _, _, _, _, _ = G
    print(len(V))


def antallKanter(G):
    V, _, w, _, _, _ = G
    antallKanter = 0
    for node in w.keys():
        antallKanter += len(w[node]) / 2
    print(int(antallKanter))



def readFromFileMovies():
    # tt-id Tittel Rating AntallStemmer

    movieIdToName = dict()
    movieRating = dict()
    with open('oblig2/movies.tsv', encoding='utf8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')

        for line in csvreader:
            data = line
            id = data[0]
            tittel = data[1]
            rating = data[2]
            movieRating[id] = rating
            movieIdToName[id] = tittel

    return movieIdToName, movieRating


def readFromFileActors():
    # nm-id Navn tt-id1 tt-id2 . . . tt-idk
    actorToMovies = {}
    idToName = {}

    with open('oblig2/actors.tsv', encoding='utf8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')

        for line in csvreader:
            data = line
            id = data[0]
            name = data[1]
            movies = set()

            for movie in data[2:]:
                movies.add(movie)

            actorToMovies[id] = movies
            idToName[id] = name

    return actorToMovies, idToName

 
def kortesteVei(G, fra, til):
    V, E, w, idToName, movieIdToName, _ = G
    
    Q = [(0, fra)]
    D = defaultdict(lambda: float('inf'))
    D[fra] = 0
    parents = {fra: None}


    while Q:
        cost, v = heappop(Q)
        if v == til:
            break
        
        for u in E[v]:
            listeOverFilmer = w[(v, u)]
            # Lager tuppel hvor rating er første verdien imens filmid er andre 
            minsteTuppel = max(listeOverFilmer)
            minsteVerdi = 10 - minsteTuppel[0]
            minsteId = minsteTuppel[1]
            c = cost + minsteVerdi
            if c < D[u]:
                D[u] = c
                heappush(Q, (c, u))
                parents[u] = (v, minsteId)

    return skrivKortesteVei(G, parents, fra, til)


def skrivKortesteVei(G, parents, fra, til):
    V, E, w, idToName, movieIdToName, movieRating = G

    current = parents[til]
    listeData = []

    while current and current[0] in parents:
        skuspillerID = current[0]
        listeData.append([current[0], current[1]])

        current = parents[skuspillerID]

    strenge = ""
    listeData.reverse()
    totalvekt = 0
    for linje in listeData:
        skuspillerID = linje[0]
        filmID = linje[1]
        skuespillerNavn = idToName[skuspillerID]
        filmNavn = movieIdToName[filmID]

        strenge += skuespillerNavn + "\n" + \
            "===[" + filmNavn + \
            " ( " + movieRating[filmID] + " ) " + "]" + "===> "
        totalvekt += 10 - float(movieRating[filmID])

    strenge += str(idToName[til] + "\n" +
                   "Total weight: " + ("%.1f" % totalvekt) + "\n")

    return strenge

def bfsShortestPath(G, fra, til):
    _, E, w, idToName, movieIdToName, movieRating = G
    parents = {fra: None}
    queue = deque([fra])
    result = []

    while queue:
        v = deque.popleft(queue)
        result.append(v)
        if v == til:
            break
        for neighbor in E[v]:
            if neighbor not in parents:
                listeOverFilmer = w[(v, neighbor)]
                filmratingOgId = listeOverFilmer[0]
                filmId = filmratingOgId[1]
                parents[neighbor] = (v, filmId)
                queue.append(neighbor)

    return parents

def shortestPathBetween(G, fra, til):
    parents = bfsShortestPath(G, fra, til)
    current = parents[til]
    path = []
    _, E, w, idToName, movieIdToName, movieRating = G

    if til not in parents:
        return path

    while current and current[0] in parents:
        skuspillerID = current[0]
        path.append([current[0], current[1]])

        current = parents[skuspillerID]

    linjeData =  path[::-1]

    strenge = ""
    for linje in linjeData:
        skuspillerID = linje[0]
        filmID = linje[1]
        skuespillerNavn = idToName[skuspillerID]
        filmNavn = movieIdToName[filmID]

        strenge += skuespillerNavn + "\n" + \
            "===[" + filmNavn + \
            " ( " + movieRating[filmID] + " ) " + "]" + "===> "
            
    strenge += str(idToName[til] + "\n")

    return strenge

def komponenter(G):
    V, E, _, _, _, _ = G

    antallAvStorrelse = defaultdict(int) #antallAvStorrelse[storrelse] = antall

    alleKomponenter = []
    alleVisited = set()

    for s in V:
        if s in alleVisited:
            continue

        visited = set([s])
        stack = [s]
        result = []

        while stack:
            v = stack.pop()
            result.append(v)
            for u in E[v]:
                if u not in visited:
                    visited.add(u)
                    alleVisited.add(u)
                    stack.append(u)
        alleKomponenter.append(result)
    
    for komponent in alleKomponenter:
        l = len(komponent)
        antallAvStorrelse[l] += 1

    


    return antallAvStorrelse


def utskriftKomponenter(G):

    antallAvStorrelse = komponenter(G)

    dictionary_items = antallAvStorrelse.items()

    sorted_items = sorted(dictionary_items, reverse=True)
    
    strenge = ""
    for storrelseAntall in sorted_items:
        strenge += f"There are {storrelseAntall[1]} components of size {storrelseAntall[0]} \n"
    
    return strenge


def main():
    #Oppgave 1
    G = buildgraph()
    print("Oppgave 1: \n")
    antallNoder(G)
    antallKanter(G)

    #Oppgave 2
    print("Oppgave 2: \n")
    print(shortestPathBetween(G, 'nm2255973', 'nm0000460'))
    print(shortestPathBetween(G, 'nm0424060', 'nm0000243'))
    print(shortestPathBetween(G, 'nm4689420', 'nm0000365'))
    print(shortestPathBetween(G, 'nm0000288', 'nm0001401'))
    print(shortestPathBetween(G, 'nm0031483', 'nm0931324'))

    #Oppgave 3
    print("Oppgave 3: \n")
    print(kortesteVei(G, 'nm2255973', 'nm0000460'))
    print(kortesteVei(G, 'nm0424060', 'nm0000243'))
    print(kortesteVei(G, 'nm4689420', 'nm0000365'))
    print(kortesteVei(G, 'nm0000288', 'nm0001401'))
    print(kortesteVei(G, 'nm0031483', 'nm0931324'))

    #oppgave 4
    print("Oppgave 4: \n")
    print(utskriftKomponenter(G))

main()
