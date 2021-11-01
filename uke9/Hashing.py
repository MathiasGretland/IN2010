import random

#En inkonsistent hashfunksjon
#Input: En nøkkel k og et positivt heltall N
#Output: Et heltall i slik at 0 <= i < N
#Dis is garbage, bcuz its not a funksjon
def inconsistent(k, N):
    return random.randint(0, N-1)



#FOR Å HASHE EN STRENG KAN VI SE PÅ HVER BOKSTAV SOM ET TALL! ALTSÅ SE PÅ ASCII TABELLEN FOR Å SE HVILKET TALL HVER BOKSTAV HAR.
#Her kan man bruke chr() for tall slik: chr(97) som da blir "a", eller så bruker man ord() for bokstaver slik: ord("a") som da blir 97'

#En god hashfunksjon på strenger
#Input: En streng s og et positivt heltall N
#Output: Et heltall h slik at 0 <= h < N
def hashString(s, N):
    h = 0
    for bokstav in s: 
        h = 31 * h + ord(bokstav)
    return h % N

print(hashString("mordi", 5))    