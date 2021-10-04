from collections import defaultdict
import graphviz
from collections import deque
import heapq


class Graf:
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

    def drawgraph(G):
        V, E, w = G
        dot = graphviz.Graph()
        seen_edges = set()

        for v in V:
            dot.node(v)

            for u in E[v]:
                if (u, v) in seen_edges:
                    continue
                seen_edges.add((v, u))
                dot.edge(v, u, label=str(w[(v, u)]))

        dot.render('graph', format='svg', view=True)

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

    def bfs(G, s):
        _, E, _ = G
        visited = set([s])
        queue = deque([s])
        resultat = []

        while queue:
            v = deque.popleft(queue)
            resultat.append(v)
            for u in E[v]:
                if u not in visited:
                    visited.add(u)
                    queue.append(u)
        return resultat

    def bfs_shortest_paths_from(G, s):
        _, E, _ = G
        parents = {s: None}
        queue = deque([s])
        result = []

        while queue:
            v = deque.popleft(queue)
            result.append(v)
            for u in E[v]:
                if u not in parents:
                    parents[u] = v
                    queue.append(u)

        return parents

    def draw_parents(parents):
        dot = graphviz.Graph()
        for v in parents:
            u = parents[v]
            if u:
                dot.edge(v, u)
        dot.render('bfs_spanningtree', format='svg', view=True)

    def dijkstra(G, s):
        _, E, w = G
        # Husk at når man legger til i queue så må du bruke HeapQ
        queue = [(0,s)]
        D = defaultdict(lambda: float('inf'))
        D[s] = 0
        
        while queue:
            cost, v = heapq.heappop(queue)
            for u in E[v]:
                c = cost + w[(v,u)]
                if c < D[u]:
                    D[u] = c
                    heapq.heappush(queue, (c,u))

        return D

def main():
    lines = open("uke5/lines.txt", "r")
    G = Graf.buildgraph(lines)
    # Graf.drawgraph(G)
    dfsResultat = Graf.dfs(G, 'A')
    print(dfsResultat)

    bfsResultat = Graf.bfs(G, 'A')
    print(bfsResultat)

    bfsShortestResultat = Graf.bfs_shortest_paths_from(G, 'A')
    print(bfsShortestResultat)
    #Graf.draw_parents(bfsShortestResultat)
    print()
    print()

    dijkstra = Graf.dijkstra(G, 'A')
    #Graf.drawgraph(dijkstra)

main()
