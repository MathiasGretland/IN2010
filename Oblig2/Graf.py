from collections import defaultdict
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

                    w[(actor, otherActor)].append(float(movieRating[movie]))
                    w[(otherActor, actor)].append(float(movieRating[movie]))

            movieActors[movie].append(actor)  # legge til skuspiller til film

    antallNoder(V)

    antallKanter(w)

    return V, E, w


def antallNoder(V):
    print(len(V))


def antallKanter(w):
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


graf = buildgraph()
