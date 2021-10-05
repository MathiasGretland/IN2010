from collections import defaultdict
import csv


def buildgraph():

    V = set()
    E = defaultdict(set)
    w = dict()
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

            # kan hende vi maa sjekke lengde istedenfor fordi den har default value
            if len(movieActors[movie]) > 0:
                for otherActor in movieActors[movie]:

                    if movie in movieRating:
                        E[actor].add(otherActor)
                        E[otherActor].add(actor)

                        w[(actor, otherActor)] = float(movieRating[movie])
                        w[(otherActor, actor)] = float(movieRating[movie])

            movieActors[movie].append(actor)  # legge til skuspiller til film

    antallNoder(V)

    print(len(movieRating))
    print(len(w)/2)
    return V, E, w


def antallNoder(V):
    print(len(V))


def antallKanter():
    pass


def readFromFileMovies():
    # tt-id Tittel Rating AntallStemmer
    tsv_file = open('oblig2/movies.tsv')
    file = csv.reader(tsv_file, delimiter="\t")
    movieIdToName = dict()
    movieRating = dict()

    for line in file:
        data = line
        id = data[0]
        tittel = data[1]
        rating = data[2]
        movieRating[id] = rating
        movieIdToName[id] = tittel
    tsv_file.close()
    return movieIdToName, movieRating


def readFromFileActors():
    # nm-id Navn tt-id1 tt-id2 . . . tt-idk
    tsv_file = open('oblig2/actors.tsv')
    file = csv.reader(tsv_file, delimiter="\t")
    actorToMovies = {}
    idToName = {}

    for line in file:
        data = line
        id = data[0]
        name = data[1]
        movies = set()

        for movie in data[2:]:
            movies.add(movie)

        actorToMovies[id] = movies
        idToName[id] = name
    tsv_file.close()
    return actorToMovies, idToName


graf = buildgraph()
