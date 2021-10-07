from collections import defaultdict
import csv
from heapq import heappop, heappush


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

        sjekk = E[v]
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
    for linje in listeData:
        skuspillerID = linje[0]
        filmID = linje[1]
        skuespillerNavn = idToName[skuspillerID]
        filmNavn = movieIdToName[filmID]

        strenge += skuespillerNavn + "\n" + \
            "===[" + filmNavn + \
            " ( " + movieRating[filmID] + " ) " + "]" + "===> "

    strenge += str(idToName[til])

    return strenge

# Vi må huske å legge til total vekt


G = buildgraph()
antallNoder(G)

antallKanter(G)

parents = kortesteVei(G, 'nm2255973', 'nm0000460')
print(parents)
print()

parents = kortesteVei(G, 'nm0424060', 'nm0000243')
print(parents)
print()

parents = kortesteVei(G, 'nm4689420', 'nm0000365')
print(parents)
print()

parents = kortesteVei(G, 'nm0000288', 'nm0001401')
print(parents)
print()

parents = kortesteVei(G, 'nm0031483', 'nm0931324')
print(parents)
