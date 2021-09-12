def lesFraFil():

    map = {}

    kattunge = input()

    current = input()

    while current != "-1":
        delt = current.split()
        forelder = delt[0]

        for i in range(1, len(delt)):
            barn = delt[i]
            map[barn] = forelder

        current = input()

    return stiFinner(kattunge, map)


def stiFinner(kattunge, map):
    strenge = str(kattunge)

    current = map[kattunge]

    while current in map:
        strenge += " " + str(current)
        current = map[current]
    strenge += " " + str(current)
    return strenge

print(lesFraFil())