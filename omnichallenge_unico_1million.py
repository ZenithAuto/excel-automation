# omnichallenge_unico_1million.py
# Programa avanzado "todo en uno" para grafos y análisis: Dijkstra con conteo de caminos,
# Kruskal MST, Tarjan SCC, puntos de articulación y puentes, diámetro aproximado,
# y resumen estructurado. Ideal para probar tu dominio.
#
# Uso: ejecutar y pegar la entrada por stdin. El programa imprime
# un informe completo del grafo y rutas cortas.

import sys
import math
import heapq
from collections import defaultdict, deque

MOD = 10**9 + 7
INF = 10**18

def dijkstra_count_paths(n, adj, src):
    dist = [INF] * (n + 1)
    ways = [0] * (n + 1)
    dist[src] = 0
    ways[src] = 1
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                ways[v] = ways[u]
                heapq.heappush(pq, (nd, v))
            elif nd == dist[v]:
                ways[v] = (ways[v] + ways[u]) % MOD
    return dist, ways

# Kruskal for MST (undirected)
class DSU:
    def __init__(self, n):
        self.p = list(range(n + 1))
        self.r = [0] * (n + 1)

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.r[ra] < self.r[rb]:
            self.p[ra] = rb
        else:
            self.p[rb] = ra
            if self.r[ra] == self.r[rb]:
                self.r[ra] += 1
        return True

# Tarjan SCC
def tarjan_scc(n, gadj):
    sys.setrecursionlimit(10000)
    index = 0
    indices = [0] * (n + 1)
    low = [0] * (n + 1)
    onstack = [False] * (n + 1)
    stack = []
    sccs = []

    def strong(v):
        nonlocal index
        index += 1
        indices[v] = index
        low[v] = index
        stack.append(v)
        onstack[v] = True
        for w in gadj[v]:
            if indices[w] == 0:
                strong(w)
                low[v] = min(low[v], low[w])
            elif onstack[w]:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            comp = []
            while True:
                w = stack.pop()
                onstack[w] = False
                comp.append(w)
                if w == v:
                    break
            sccs.append(comp)

    for v in range(1, n + 1):
        if indices[v] == 0:
            strong(v)
    return sccs

# Articulation points and Bridges (undirected)
def articulation_bridges(n, adj_undirected):
    sys.setrecursionlimit(10000)
    tin = [-1] * (n + 1)
    low = [0] * (n + 1)
    timer = 0
    visited = [False] * (n + 1)
    bridges = []
    articulation = set()

    def dfs(v, p=-1):
        nonlocal timer
        visited[v] = True
        tin[v] = low[v] = timer
        timer += 1
        children = 0
        for to, _ in adj_undirected[v]:
            if to == p:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.append((v, to))
                if low[to] >= tin[v] and p != -1:
                    articulation.add(v)
                children += 1
        if p == -1 and children > 1:
            articulation.add(v)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
    return sorted(list(articulation)), sorted(bridges)

# diameter approximation using two BFS on unweighted version of graph
def approx_diameter(n, adj_undirected):
    def bfs(f):
        dist = [-1] * (n + 1)
        q = deque([f])
        dist[f] = 0
        while q:
            u = q.popleft()
            for v, _ in adj_undirected[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist

    start = 1
    for i in range(1, n + 1):
        if adj_undirected[i]:
            start = i
            break

    d1 = bfs(start)
    far = max(range(1, n + 1), key=lambda x: d1[x] if d1[x] != -1 else -1)
    d2 = bfs(far)
    far2 = max(range(1, n + 1), key=lambda x: d2[x] if d2[x] != -1 else -1)
    diameter = d2[far2] if d2[far2] != -1 else 0
    return diameter, far, far2

# read graph and run full analysis
def analyze_all():
    data = sys.stdin.read().strip().split()
    if not data:
        print("No input provided.")
        return

    it = iter(data)
    try:
        n = int(next(it))
    except StopIteration:
        print("Invalid input")
        return
    m = int(next(it))

    edges = []
    adj = [[] for _ in range(n + 1)]
    adj_undirected = [[] for _ in range(n + 1)]
    gadj = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
        adj[u].append((v, w))
        adj_undirected[u].append((v, w))
        adj_undirected[v].append((u, w))
        gadj[u].append(v)

    print("OMNI-REPORT")
    print("Nodes:", n, "Edges:", m)
    print()

    all_dist = {}
    all_ways = {}
    cap = 100
    compute_nodes = list(range(1, n + 1)) if n <= cap else list(range(1, min(n, 10) + 1))
    print("Running Dijkstra + path counting from", len(compute_nodes), "sources (cap at", cap, ")")

    for s in compute_nodes:
        dist, ways = dijkstra_count_paths(n, adj, s)
        all_dist[s] = dist
        all_ways[s] = ways

    print()
    print("SAMPLE DISTANCES (source -> [target:dist (#ways)])")
    for s in compute_nodes[:min(5, len(compute_nodes))]:
        line = []
        for t in range(1, min(n, 10) + 1):
            d = all_dist[s][t]
            w = all_ways[s][t]
            if d >= INF:
                line.append(f"{t}:INF")
            else:
                line.append(f"{t}:{d}({w})")
        print(f"src {s} ->", ", ".join(line))
    print()

    undirected_edges = {}
    for u, v, w in edges:
        a, b = min(u, v), max(u, v)
        if (a, b) not in undirected_edges or undirected_edges[(a, b)] > w:
            undirected_edges[(a, b)] = w

    edge_list = [(w, a, b) for (a, b), w in undirected_edges.items()]
    edge_list.sort()
    dsu = DSU(n)
    mst_weight = 0
    mst_edges = []

    for w, a, b in edge_list:
        if dsu.union(a, b):
            mst_weight += w
            mst_edges.append((a, b, w))

    connected_components = len(set(dsu.find(i) for i in range(1, n + 1)))
    print("MST weight (if graph connected):", mst_weight)
    print("MST edges (up to 10 shown):")
    for e in mst_edges[:10]:
        print("  ", e)
    print("Connected components after Kruskal:", connected_components)
    print()

    sccs = tarjan_scc(n, gadj)
    print("SCC count:", len(sccs))
    if len(sccs) <= 10:
        for i, comp in enumerate(sccs, 1):
            print(f"  SCC {i} size={len(comp)}:", comp)
    else:
        print("  (many SCCs, showing first 10)")
        for i, comp in enumerate(sccs[:10], 1):
            print(f"  SCC {i} size={len(comp)}:", comp)
    print()

    arts, brs = articulation_bridges(n, adj_undirected)
    print("Articulation points:", arts)
    print("Bridges:", brs[:20])
    print()

    diameter, a, b = approx_diameter(n, adj_undirected)
    print("Approximate diameter (unweighted):", diameter, "between nodes", a, "and", b)
    print()

    if n <= 50:
        print("All-pairs sample distances matrix (INF means unreachable):")
        for s in compute_nodes:
            row = []
            for t in range(1, n + 1):
                d = all_dist[s][t] if s in all_dist else INF
                row.append("INF" if d >= INF else str(d))
            print(" ".join(row))
        print()

    print("END OF OMNI-REPORT")
    print("Notes:")
    print(" - Distances computed for a subset if n large (cap).")
    print(" - MST computed on undirected projection.")
    print(" - SCC uses directed edges input.")
    print(" - Articulation points and bridges computed on undirected projection.")

if __name__ == "__main__":
    analyze_all()