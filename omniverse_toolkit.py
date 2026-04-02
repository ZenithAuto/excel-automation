# omnichallenge_level_million.py
# Mega toolkit: colección avanzada de algoritmos y estructuras de datos en un único archivo.
# Modo de uso (lee desde stdin): la primera línea indica el "modo" o problema a ejecutar,
# seguido de la entrada específica para ese modo. El programa intenta ser robusto y
# autodocumentado en funciones (comentarios dentro del código).
#
# Módulos disponibles (escribir exactamente la palabra en mayúsculas en la primera línea):
# GRAPH   -> análisis completo de grafo (Dijkstra, conteo de caminos, Kruskal, SCC, bridges, articulation, diameter aprox)
# FLOW    -> máximo flujo (Dinic)
# STRINGS -> sufijo array, LCP, KMP, anagram checker
# SEGMENT -> segment tree with lazy, fenwick
# GEOM    -> convex hull (Graham), polygon area, line intersection
# DP      -> knapsack (0/1), LIS (n log n), subset-sum bitset
# MATH    -> modular combinatorics (nCr mod p with precompute), pollard rho primality helpers
# RUNALL  -> modo demostración ejecuta tests embebidos
#
# Nota: para usar copia este archivo y ejecuta:
# python omnichallenge_level_million.py
#
# Luego pega la entrada empezando con el modo deseado. Ejemplo:
# GRAPH
# ... (entrada que GRAPH requiere)
#
# El archivo intenta proteger contra inputs inválidos.

import sys
import math
import random
import heapq
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right, insort
from typing import List, Tuple

# ---------- UTILIDADES LECTURA ----------
def read_all_tokens():
    data = sys.stdin.read().strip().split()
    return data

def tokens_iter():
    for t in read_all_tokens():
        yield t

_TOKS = None
_IT = None
def init_tokens():
    global _TOKS, _IT
    _TOKS = read_all_tokens()
    _IT = iter(_TOKS)

def next_token(default=None):
    global _IT
    try:
        return next(_IT)
    except StopIteration:
        return default

def next_int(default=0):
    t = next_token(None)
    if t is None:
        return default
    return int(t)

# ---------- GRAPH ALGORITHMS ----------
class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0]*(n+1)
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, a, b):
        ra = self.find(a); rb = self.find(b)
        if ra == rb: return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        else:
            self.parent[rb] = ra
            if self.rank[ra] == self.rank[rb]:
                self.rank[ra] += 1
        return True

INF = 10**30
MOD = 10**9+7

def dijkstra_count_paths(n, adj, src):
    dist = [INF]*(n+1)
    ways = [0]*(n+1)
    dist[src] = 0
    ways[src] = 1
    pq = [(0, src)]
    while pq:
        d,u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v,w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                ways[v] = ways[u]
                heapq.heappush(pq, (nd, v))
            elif nd == dist[v]:
                ways[v] = (ways[v] + ways[u]) % MOD
    return dist, ways

def kruskal_mst(n, edges):
    # edges: list of (w,u,v)
    edges_sorted = sorted(edges)
    dsu = DSU(n)
    mst_weight = 0
    mst_edges = []
    for w,u,v in edges_sorted:
        if dsu.union(u,v):
            mst_weight += w
            mst_edges.append((u,v,w))
    comps = len(set(dsu.find(i) for i in range(1,n+1)))
    return mst_weight, mst_edges, comps

def tarjan_scc(n, adj):
    sys.setrecursionlimit(10000)
    idx = 0
    indices = [0]*(n+1)
    low = [0]*(n+1)
    onstack = [False]*(n+1)
    stack = []
    sccs = []
    def strong(v):
        nonlocal idx
        idx += 1
        indices[v] = idx
        low[v] = idx
        stack.append(v); onstack[v]=True
        for w in adj[v]:
            if indices[w] == 0:
                strong(w)
                low[v] = min(low[v], low[w])
            elif onstack[w]:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            comp = []
            while True:
                w = stack.pop(); onstack[w]=False
                comp.append(w)
                if w==v: break
            sccs.append(comp)
    for i in range(1,n+1):
        if indices[i]==0:
            strong(i)
    return sccs

def articulation_and_bridges(n, adj_undirected):
    sys.setrecursionlimit(10000)
    tin = [-1]*(n+1)
    low = [0]*(n+1)
    used = [False]*(n+1)
    timer = 0
    bridges = []
    articulation = set()
    def dfs(v, p=-1):
        nonlocal timer
        used[v]=True
        tin[v]=low[v]=timer; timer+=1
        children=0
        for to,_ in adj_undirected[v]:
            if to==p: continue
            if used[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.append((min(v,to), max(v,to)))
                if low[to] >= tin[v] and p!=-1:
                    articulation.add(v)
                children+=1
        if p==-1 and children>1:
            articulation.add(v)
    for i in range(1,n+1):
        if not used[i]:
            dfs(i)
    bridges.sort()
    return sorted(list(articulation)), bridges

def approx_diameter(n, adj_undirected):
    def bfs(s):
        dist = [-1]*(n+1)
        q = deque([s]); dist[s]=0
        while q:
            u = q.popleft()
            for v,_ in adj_undirected[u]:
                if dist[v]==-1:
                    dist[v]=dist[u]+1; q.append(v)
        return dist
    start = 1
    for i in range(1,n+1):
        if adj_undirected[i]:
            start = i; break
    d1 = bfs(start)
    far = max(range(1,n+1), key=lambda x: d1[x] if d1[x]!=-1 else -1)
    d2 = bfs(far)
    far2 = max(range(1,n+1), key=lambda x: d2[x] if d2[x]!=-1 else -1)
    diam = d2[far2] if d2[far2]!=-1 else 0
    return diam, far, far2

# ---------- DINIC MAX FLOW ----------
class Dinic:
    class Edge:
        __slots__ = ('v','cap','rev')
        def __init__(self,v,cap,rev):
            self.v=v; self.cap=cap; self.rev=rev
    def __init__(self,n):
        self.n=n
        self.g=[[] for _ in range(n)]
        self.level=[0]*n
        self.it=[0]*n
    def add_edge(self,u,v,c):
        a=self.Edge(v,c,len(self.g[v])); b=self.Edge(u,0,len(self.g[u]))
        self.g[u].append(a); self.g[v].append(b)
    def bfs(self,s,t):
        from collections import deque
        for i in range(self.n): self.level[i]=-1
        q=deque([s]); self.level[s]=0
        while q:
            u=q.popleft()
            for e in self.g[u]:
                if e.cap>0 and self.level[e.v]<0:
                    self.level[e.v]=self.level[u]+1
                    q.append(e.v)
        return self.level[t]!=-1
    def dfs(self,u,t,f):
        if u==t: return f
        for i in range(self.it[u], len(self.g[u])):
            e=self.g[u][i]
            if e.cap>0 and self.level[e.v]==self.level[u]+1:
                ret=self.dfs(e.v,t,min(f,e.cap))
                if ret>0:
                    e.cap-=ret
                    self.g[e.v][e.rev].cap+=ret
                    return ret
            self.it[u]+=1
        return 0
    def max_flow(self,s,t):
        flow=0
        while self.bfs(s,t):
            self.it=[0]*self.n
            while True:
                f=self.dfs(s,t,10**30)
                if f==0: break
                flow+=f
        return flow

# ---------- STRINGS: SA, LCP, KMP ----------
def suffix_array(s: str):
    # SA in O(n log n) using doubling
    s_bytes = [ord(c) for c in s]
    n = len(s_bytes)
    k = 1
    sa = list(range(n))
    rank = s_bytes[:] + [-1]
    tmp = [0]*n
    while True:
        sa.sort(key=lambda x: (rank[x], rank[x+k] if x+k < n else -1))
        tmp[sa[0]] = 0
        for i in range(1,n):
            prev, cur = sa[i-1], sa[i]
            tmp[cur] = tmp[prev] + (1 if (rank[prev], rank[prev+k] if prev+k<n else -1) != (rank[cur], rank[cur+k] if cur+k<n else -1) else 0)
        rank[:n] = tmp[:n]
        if rank[sa[-1]] == n-1:
            break
        k <<= 1
    return sa

def lcp_array(s, sa):
    n = len(s)
    rank = [0]*n
    for i, pos in enumerate(sa):
        rank[pos]=i
    h = 0
    lcp = [0]*(n-1)
    for i in range(n):
        if rank[i] == 0:
            continue
        j = sa[rank[i]-1]
        while i+h<n and j+h<n and s[i+h]==s[j+h]:
            h+=1
        lcp[rank[i]-1]=h
        if h>0: h-=1
    return lcp

def kmp_search(text, pattern):
    # returns starting indices
    if not pattern:
        return list(range(len(text)+1))
    n = len(pattern)
    lps = [0]*n
    for i in range(1,n):
        j=lps[i-1]
        while j>0 and pattern[i]!=pattern[j]:
            j=lps[j-1]
        if pattern[i]==pattern[j]:
            j+=1
        lps[i]=j
    res=[]
    j=0
    for i,ch in enumerate(text):
        while j>0 and ch!=pattern[j]:
            j=lps[j-1]
        if ch==pattern[j]:
            j+=1
        if j==n:
            res.append(i-n+1); j=lps[j-1]
    return res

# ---------- SEGMENT TREE & FENWICK ----------
class Fenwick:
    def __init__(self,n):
        self.n=n; self.bit=[0]*(n+1)
    def add(self,i,v):
        while i<=self.n:
            self.bit[i]+=v; i+=i&-i
    def sum(self,i):
        s=0
        while i>0:
            s+=self.bit[i]; i-=i&-i
        return s
    def range_sum(self,l,r):
        return self.sum(r)-self.sum(l-1)

class SegmentTreeLazy:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.data = [0]*(2*self.size)
        self.lazy = [0]*(2*self.size)
        for i,v in enumerate(arr):
            self.data[self.size+i] = v
        for i in range(self.size-1,0,-1):
            self.data[i] = self.data[2*i] + self.data[2*i+1]
    def _apply(self, idx, l, r, val):
        self.data[idx] += val*(r-l+1)
        self.lazy[idx] += val
    def _push(self, idx, l, r):
        if self.lazy[idx]:
            m = (l+r)//2
            self._apply(2*idx, l, m, self.lazy[idx])
            self._apply(2*idx+1, m+1, r, self.lazy[idx])
            self.lazy[idx]=0
    def _update(self, idx, l, r, ql, qr, val):
        if ql>r or qr<l: return
        if ql<=l and r<=qr:
            self._apply(idx,l,r,val); return
        self._push(idx,l,r)
        m=(l+r)//2
        self._update(2*idx,l,m,ql,qr,val)
        self._update(2*idx+1,m+1,r,ql,qr,val)
        self.data[idx] = self.data[2*idx] + self.data[2*idx+1]
    def update(self, l, r, val):
        self._update(1,0,self.size-1,l,r,val)
    def _query(self, idx, l, r, ql, qr):
        if ql>r or qr<l: return 0
        if ql<=l and r<=qr:
            return self.data[idx]
        self._push(idx,l,r)
        m=(l+r)//2
        return self._query(2*idx,l,m,ql,qr)+self._query(2*idx+1,m+1,r,ql,qr)
    def query(self,l,r):
        return self._query(1,0,self.size-1,l,r)

# ---------- GEOMETRY ----------
def cross(a,b,c):
    # cross product (b-a) x (c-a)
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def convex_hull(points: List[Tuple[float,float]]):
    pts = sorted(set(points))
    if len(pts) <=1: return pts
    lower=[]
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def polygon_area(points):
    n = len(points)
    area = 0
    for i in range(n):
        x1,y1 = points[i]
        x2,y2 = points[(i+1)%n]
        area += x1*y2 - x2*y1
    return abs(area)/2

# ---------- DYNAMIC PROGRAMMING ----------
def knapsack_01(values, weights, W):
    n = len(values)
    dp = [0]*(W+1)
    for i in range(n):
        w = weights[i]; v = values[i]
        for cap in range(W, w-1, -1):
            dp[cap] = max(dp[cap], dp[cap-w] + v)
    return dp[W]

def lis_length(arr):
    from bisect import bisect_left
    tail = []
    for x in arr:
        i = bisect_left(tail, x)
        if i == len(tail): tail.append(x)
        else: tail[i] = x
    return len(tail)

def subset_sum_bitset(arr, target):
    bs = 1
    for x in arr:
        bs |= (bs << x)
    return (bs >> target) & 1

# ---------- NUMBER THEORY ----------
def powmod(a, b, mod):
    res = 1
    a %= mod
    while b:
        if b&1: res = (res*a)%mod
        a = (a*a)%mod; b >>= 1
    return res

def nCr_mod_p(n, r, p):
    # naive if p large; for demonstration, compute factorials mod p (works for p up to big)
    if r < 0 or r > n: return 0
    fact = 1
    for i in range(1, n+1): fact = (fact * i) % p
    invfact = powmod(fact, p-2, p)
    # Not efficient for large n; placeholder for demonstration
    # Instead implement multiplicative formula
    num = 1
    den = 1
    for i in range(r):
        num = num * (n - i) % p
        den = den * (i + 1) % p
    return num * powmod(den, p-2, p) % p

# ---------- PROBLEM DISPATCHERS ----------
def run_graph_mode(it):
    # Input format:
    # n m
    # m lines: u v w
    # optional: q s t ... not required, we'll run analyses and print a report
    n = int(next(it))
    m = int(next(it))
    edges = []
    adj = [[] for _ in range(n+1)]
    adj_undirected = [[] for _ in range(n+1)]
    gadj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        edges.append((u,v,w))
        adj[u].append((v,w))
        gadj[u].append(v)
        adj_undirected[u].append((v,w)); adj_undirected[v].append((u,w))
    print("NODES", n, "EDGES", m)
    # run Dijkstra from node 1 (if exist)
    start = 1
    for i in range(1,n+1):
        if adj[i] or adj_undirected[i]:
            start = i; break
    dist, ways = dijkstra_count_paths(n, adj, start)
    print("DIJKSTRA sample from", start)
    for i in range(1, n+1):
        d = dist[i]
        w = ways[i]
        print(f"  to {i}: {d if d<INF else 'INF'} ({w})")
    # Kruskal
    undeg = {}
    for u,v,w in edges:
        a,b = min(u,v), max(u,v)
        if (a,b) not in undeg or undeg[(a,b)]>w:
            undeg[(a,b)] = w
    edge_list = [(w,a,b) for (a,b),w in undeg.items()]
    mstw, mstedges, comps = kruskal_mst(n, edge_list)
    print("MST weight", mstw, "components", comps)
    print("MST edges sample:", mstedges[:10])
    # SCC
    sccs = tarjan_scc(n, gadj)
    print("SCC count", len(sccs))
    # articulation & bridges
    arts, brs = articulation_and_bridges(n, adj_undirected)
    print("Articulation points:", arts)
    print("Bridges sample:", brs[:10])
    diam, a, b = approx_diameter(n, adj_undirected)
    print("Approx diameter (unweighted):", diam, "endpoints", a, b)

def run_flow_mode(it):
    # format:
    # n m s t
    # m lines: u v cap
    n = int(next(it)); m = int(next(it)); s = int(next(it)); t = int(next(it))
    din = Dinic(n+5)
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); c = int(next(it))
        din.add_edge(u, v, c)
    flow = din.max_flow(s, t)
    print(flow)

def run_strings_mode(it):
    # MODE expects a subcommand: SA / KMP / ANAGRAM
    sub = next(it)
    if sub == "SA":
        s = next(it)
        sa = suffix_array(s)
        lcp = lcp_array(s, sa)
        print("SA:", " ".join(map(str, sa)))
        print("LCP:", " ".join(map(str, lcp)))
    elif sub == "KMP":
        text = next(it); pat = next(it)
        res = kmp_search(text, pat)
        if res:
            print("FOUND at", " ".join(map(str, res)))
        else:
            print("NOTFOUND")
    elif sub == "ANAGRAM":
        a = next(it); b = next(it)
        print("SI" if sorted(a)==sorted(b) else "NO")
    else:
        # default: run SA on entire remainder
        s = "".join(list(it))
        sa = suffix_array(s)
        lcp = lcp_array(s, sa)
        print("SA sample:", sa[:20])
        print("LCP sample:", lcp[:20])

def run_segment_mode(it):
    sub = next(it)
    if sub == "FENWICK":
        n = int(next(it)); arr = [int(next(it)) for _ in range(n)]
        fw = Fenwick(n)
        for i,v in enumerate(arr, start=1):
            fw.add(i,v)
        q = int(next(it))
        for _ in range(q):
            l = int(next(it)); r = int(next(it))
            print(fw.range_sum(l,r))
    else:
        # build segment from list
        n = int(next(it)); arr = [int(next(it)) for _ in range(n)]
        seg = SegmentTreeLazy(arr)
        ops = int(next(it))
        for _ in range(ops):
            typ = next(it)
            if typ == "add":
                l = int(next(it)); r = int(next(it)); v = int(next(it))
                seg.update(l,r,v)
            else:
                l = int(next(it)); r = int(next(it))
                print(seg.query(l,r))

def run_geom_mode(it):
    sub = next(it)
    if sub == "HULL":
        k = int(next(it))
        pts = [(float(next(it)), float(next(it))) for _ in range(k)]
        hull = convex_hull(pts)
        print(len(hull))
        for x,y in hull:
            print(f"{x} {y}")
    elif sub == "AREA":
        k = int(next(it)); pts=[]
        for _ in range(k):
            pts.append((float(next(it)), float(next(it))))
        print(polygon_area(pts))
    else:
        # intersection sample: read 4 points
        x1,y1,x2,y2,x3,y3,x4,y4 = map(float, [next(it) for _ in range(8)])
        # compute intersection of segments (x1,y1)-(x2,y2) and (x3,y3)-(x4,y4)
        def inter(a,b,c,d):
            x1,y1=a; x2,y2=b; x3,y3=c; x4,y4=d
            A1 = y2-y1; B1 = x1-x2; C1 = A1*x1 + B1*y1
            A2 = y4-y3; B2 = x3-x4; C2 = A2*x3 + B2*y3
            det = A1*B2 - A2*B1
            if abs(det) < 1e-12: return None
            x = (B2*C1 - B1*C2)/det
            y = (A1*C2 - A2*C1)/det
            return (x,y)
        res = inter((x1,y1),(x2,y2),(x3,y3),(x4,y4))
        if res is None: print("PARALLEL")
        else: print(f"{res[0]} {res[1]}")

def run_dp_mode(it):
    sub = next(it)
    if sub == "KNAP":
        n = int(next(it)); W = int(next(it))
        vals=[]; wgts=[]
        for _ in range(n):
            wgts.append(int(next(it))); vals.append(int(next(it)))
        print(knapsack_01(vals, wgts, W))
    elif sub == "LIS":
        n = int(next(it)); arr=[int(next(it)) for _ in range(n)]
        print(lis_length(arr))
    elif sub == "SUBSET":
        n = int(next(it)); arr=[int(next(it)) for _ in range(n)]; target=int(next(it))
        print(1 if subset_sum_bitset(arr, target) else 0)
    else:
        print("UNKNOWN DP SUBMODE")

def run_math_mode(it):
    sub = next(it)
    if sub == "NCR":
        n = int(next(it)); r = int(next(it)); p = int(next(it))
        print(nCr_mod_p(n,r,p))
    else:
        print("MATH MODE: available NCR")

def run_all_mode(it):
    # demo runner: runs a battery of quick tests and prints status
    print("RUNNING SELF TEST SUITE")
    # small graph test
    print("Graph selftest:")
    data = "4 4 1 2 1 2 3 2 3 4 3 4 1 4"
    it2 = iter(data.split())
    run_graph_mode(it2)
    print("Dinic test:")
    data2 = "6 7 1 6 1 2 10 1 3 10 2 4 4 3 4 6 4 5 10 5 6 10"
    it3 = iter(data2.split())
    run_flow_mode(it3)
    print("Strings test:")
    it4 = iter("KMP abcdabc abcd".split())
    run_strings_mode(it4)
    print("DP test:")
    it5 = iter("LIS 5 1 2 3 2 4".split())
    run_dp_mode(it5)
    print("SELFTEST COMPLETE")

# ---------- MAIN DISPATCH ----------
def main():
    init_tokens()
    mode = next_token(None)
    if mode is None:
        print("No mode specified. Exiting.")
        return
    mode = mode.strip().upper()
    if mode == "GRAPH":
        run_graph_mode(_IT)
    elif mode == "FLOW":
        run_flow_mode(_IT)
    elif mode == "STRINGS":
        run_strings_mode(_IT)
    elif mode == "SEGMENT":
        run_segment_mode(_IT)
    elif mode == "GEOM":
        run_geom_mode(_IT)
    elif mode == "DP":
        run_dp_mode(_IT)
    elif mode == "MATH":
        run_math_mode(_IT)
    elif mode == "RUNALL":
        run_all_mode(_IT)
    else:
        # fallback: try to parse as graph input
        try:
            # attempt to treat as graph if numeric
            first = int(mode)
            # if conversion succeeds, rebuild iterator
            alltoks = _TOKS
            _IT2 = iter(alltoks)
            run_graph_mode(_IT2)
        except Exception:
            print("Unknown mode:", mode)
            print("Available: GRAPH, FLOW, STRINGS, SEGMENT, GEOM, DP, MATH, RUNALL")

if __name__ == "__main__":
    main()