from collections import defaultdict
import graphviz


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


def main():
    lines = open("uke5/lines.txt", "r")
    G = Graf.buildgraph(lines)
    Graf.drawgraph(G)


main()
