
tallene = []

for i in range(1, 1001):
    tallene.append(i)

def binaerSok(arr):
    low = arr[0] # for å starte på tallet 1
    high = arr[len(arr)-1] # for å starte på taller 1000
    i = 500
    print(i)

    teller = 0
    while low < high and teller != 10:
        line = input()
        if line == "correct":
            break
        elif line == "higher":
            low = i+1
            i = int((high + low)/2)
            print(i, flush=True)
        elif line == "lower":
            high = i-1
            i = int((high + low)/2)
            print(i, flush=True)
        teller += 1


binaerSok(tallene)

#print("....", flush=True)