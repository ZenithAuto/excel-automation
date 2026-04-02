import sys
import argparse
import heapq
import csv
from collections import defaultdict, deque

INF = float("inf")

# ========================
# DIJKSTRA CON TODOS LOS CAMINOS
# ========================
def dijkstra_all_paths(graph, start):
    dist = defaultdict(lambda: INF)
    parents = defaultdict(list)
    ways = defaultdict(int)

    dist[start] = 0
    ways[start] = 1
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parents[v] = [u]
                ways[v] = ways[u]
                heapq.heappush(pq, (nd, v))
            elif nd == dist[v]:
                parents[v].append(u)
                ways[v] += ways[u]

    return dist, parents, ways


def build_all_paths(parents, start, end):
    paths = []

    def dfs(node, path):
        if node == start:
            paths.append([start] + path)
            return
        for p in parents[node]:
            dfs(p, [node] + path)

    if end != start:
        dfs(end, [])
    else:
        paths.append([start])

    return paths


# ========================
# GRAPHVIZ
# ========================
def export_graphviz(graph, filename="graph.dot"):
    with open(filename, "w") as f:
        f.write("graph G {\n")
        for u in graph:
            for v, w in graph[u]:
                if u <= v:
                    f.write(f'  {u} -- {v} [label="{w}"];\n')
        f.write("}\n")


# ========================
# MAIN
# ========================
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directed", action="store_true")
    parser.add_argument("--undirected", action="store_true")
    parser.add_argument("--solo-dijkstra", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--silent", action="store_true")

    args = parser.parse_args()

    graph = defaultdict(list)

    data = sys.stdin.read().strip().split()
    n, m = map(int, data[:2])
    idx = 2

    for _ in range(m):
        u, v, w = map(int, data[idx:idx+3])
        idx += 3
        graph[u].append((v, w))
        if not args.directed:
            graph[v].append((u, w))

    report = []
    report.append("OMNI-REPORT")
    report.append(f"Nodes: {n} Edges: {m}")
    report.append("DIJKSTRA + CAMINOS")

    csv_rows = [["from", "to", "distance", "ways", "paths"]]

    for s in range(1, n+1):
        dist, parents, ways = dijkstra_all_paths(graph, s)
        for t in range(1, n+1):
            paths = build_all_paths(parents, s, t)
            report.append(
                f"{s} -> {t}: dist={dist[t]} ways={ways[t]} path={paths[0]}"
            )
            csv_rows.append([s, t, dist[t], ways[t], paths])

    # ========================
    # EXPORTES
    # ========================
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(report))

    with open("report.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(csv_rows)

    export_graphviz(graph)

    if not args.silent:
        print("\n".join(report))
        print("END OF OMNI-REPORT")


if __name__ == "__main__":
    main()