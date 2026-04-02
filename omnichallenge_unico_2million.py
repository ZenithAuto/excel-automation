# omnichallenge_unico_1million.py
# Programa avanzado "todo en uno" para grafos y análisis:
# Dijkstra con conteo de caminos + impresión de ruta,
# Kruskal MST, Tarjan SCC, puntos de articulación y puentes,
# diámetro aproximado y reporte exportado a .txt

import sys
import heapq
from collections import deque

MOD = 10**9 + 7
INF = 10**18

# =========================
# Dijkstra con conteo + camino
# =========================
def dijkstra_count_paths(n, adj, src):
    dist = [INF] * (n + 1)
    ways = [0] * (n + 1)
    parent = [-1] * (n + 1)

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
                parent[v] = u
                heapq.heappush(pq, (nd, v))
            elif nd == dist[v]:
                ways[v] = (ways[v] + ways[u]) % MOD

    return dist, ways, parent

def reconstruir_camino(parent, src, dest):
    path = []
    while dest != -1:
        path.append(dest)
        dest = parent[dest]
    path.reverse()
    if path and path[0] == src:
        return path
    return []

# =========================
# DSU para Kruskal
# =========================
class DSU:
    def __init__(self, n):
        self.p = list(range(n+1))
        self.r = [0]*(n+1)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

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

# =========================
# Tarjan SCC
# =========================
def tarjan_scc(n, gadj):
    sys.setrecursionlimit(10000)
    index = 0
    stack = []
    onstack = [False]*(n+1)
    indices = [0]*(n+1)
    low = [0]*(n+1)
    sccs = []

    def dfs(v):
        nonlocal index
        index += 1
        indices[v] = low[v] = index
        stack.append(v)
        onstack[v] = True

        for w in gadj[v]:
            if indices[w] == 0:
                dfs(w)
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

    for i in range(1, n+1):
        if indices[i] == 0:
            dfs(i)

    return sccs

# =========================
# Articulaciones y puentes
# =========================
def articulation_bridges(n, adj):
    sys.setrecursionlimit(10000)
    timer = 0
    tin = [-1]*(n+1)
    low = [0]*(n+1)
    visited = [False]*(n+1)
    bridges = []
    art = set()

    def dfs(v, p=-1):
        nonlocal timer
        visited[v] = True
        tin[v] = low[v] = timer
        timer += 1
        children = 0

        for to, _ in adj[v]:
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
                    art.add(v)
                children += 1

        if p == -1 and children > 1:
            art.add(v)

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)

    return sorted(art), sorted(bridges)

# =========================
# Diámetro aproximado
# =========================
def approx_diameter(n, adj):
    def bfs(s):
        dist = [-1]*(n+1)
        q = deque([s])
        dist[s] = 0
        while q:
            u = q.popleft()
            for v, _ in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist

    start = 1
    for i in range(1, n+1):
        if adj[i]:
            start = i
            break

    d1 = bfs(start)
    a = max(range(1, n+1), key=lambda x: d1[x])
    d2 = bfs(a)
    b = max(range(1, n+1), key=lambda x: d2[x])

    return d2[b], a, b

# =========================
# MAIN
# =========================
def analyze_all():
    archivo = open("OMNI_REPORT.txt", "w", encoding="utf-8")

    def log(*args):
        print(*args)
        print(*args, file=archivo)

    log("Tipo de grafo:")
    log("1 = Dirigido")
    log("2 = No dirigido")
    tipo = input("Elige (1 o 2): ").strip()

    log("\nPega los datos del grafo y presiona CTRL+Z + ENTER:\n")

    data = sys.stdin.read().strip().split()
    it = iter(data)

    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n+1)]
    adj_u = [[] for _ in range(n+1)]
    gadj = [[] for _ in range(n+1)]
    edges = []

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))

        adj[u].append((v, w))
        gadj[u].append(v)

        if tipo == "2":
            adj[v].append((u, w))
            gadj[v].append(u)

        adj_u[u].append((v, w))
        adj_u[v].append((u, w))

    log("\nOMNI-REPORT")
    log("Nodes:", n, "Edges:", m)

    log("\nDIJKSTRA + CAMINOS")
    for s in range(1, n+1):
        dist, ways, parent = dijkstra_count_paths(n, adj, s)
        for t in range(1, n+1):
            if dist[t] < INF:
                camino = reconstruir_camino(parent, s, t)
                log(f"{s} -> {t}: dist={dist[t]} ways={ways[t]} path={camino}")

    und = {}
    for u, v, w in edges:
        a, b = min(u, v), max(u, v)
        if (a, b) not in und or und[(a, b)] > w:
            und[(a, b)] = w

    dsu = DSU(n)
    mst = 0
    for (a, b), w in und.items():
        if dsu.union(a, b):
            mst += w

    log("\nMST weight:", mst)

    sccs = tarjan_scc(n, gadj)
    log("\nSCC count:", len(sccs))

    art, br = articulation_bridges(n, adj_u)
    log("Articulation points:", art)
    log("Bridges:", br)

    d, a, b = approx_diameter(n, adj_u)
    log("Approx diameter:", d, "between", a, "and", b)

    log("\nEND OF OMNI-REPORT")
    archivo.close()

# EJECUCIÓN
if __name__ == "__main__":
    analyze_all()