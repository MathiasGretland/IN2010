from collections import defaultdict
from os import sep


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


def dfs(G, s):
    _, E, _ = G
    visited = set([s])
    stack = [s]
    result = []

    while stack:
        v = stack.pop()
        result.append(v)
        for u in E[v]:
            if u not in visited:
                visited.add(u)
                stack.append(u)
    return result


def dfs_rec(G, s, visited, result):
    _, E, _ = G
    result.append(s)
    visited.add(s)
    for v in E[s]:
        if v not in visited:
            dfs_rec(G, v, visited, result)
    return result


def hopcroftTarjan(G, u, depth, visited):
    _, E, _ = G
    visited.add(u)
    low = {}
    index = {}
    low[u] = depth
    index[u] = depth
    childCount = 0
    sep_vertices = set()

    for v in E[u]:
        if v not in visited:
            childCount += 1
            hopcroftTarjan(G, v, depth+1, visited)
            lowlavest1 = low.get(u)
            lowlavest2 = low.get(u)
            low[u] = min(lowlavest1, lowlavest2)
            if index[u] != 1:
                indexlavest = index.get(u)
                lowlavest3 = low.get(v)
                if indexlavest is None:
                    indexlavest = 0
                if lowlavest3 is None:
                    lowlavest3 = 0
                if indexlavest <= lowlavest3:
                    sep_vertices.add(u)
        else:
            lowlavest = low.get(u)
            indexlavest = index.get(v)
            if indexlavest is None:
                indexlavest = 0
            low[u] = min(lowlavest, indexlavest)

    if index[u] == 1:
        if childCount > 1:
            sep_vertices.add(u)

    return sep_vertices


def main():
    lines = open("uke6/lines.txt", "r")
    G = buildgraph(lines)
    rundfs = dfs(G, 'A')
    print(rundfs)
    visited = set()
    hopcroftTarjan(G, 'A', 1, visited)
    #rec = dfs_rec(G, 'A', set(), [])
    # print(rec)


main()
