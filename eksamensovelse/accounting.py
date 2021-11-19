
from collections import defaultdict


info = input().split()

antallPersoner = int(info[0])

account = defaultdict(lambda: 0)

antallEvents = int(info[1])
for i in range(antallEvents):
    inData = input().split()
    kommando = inData[0]
    
    if kommando == "RESTART":
        wealth = int(inData[1])
        account = defaultdict(lambda: wealth)

    elif kommando == "SET":
        index = int(inData[1])
        value = int(inData[2])
        account[index-1] = value
    elif kommando == "PRINT":
        index = int(inData[1])
        print(account[index-1])