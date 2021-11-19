import sys


inliste = []

for line in sys.stdin:
    inliste.append(line)

total = 0
for x in inliste[1:]:
    nums = x.split()
    for n in nums:
        total+=int(n)
    print(total)