#找割点
def dfs(u, father):
    global timer
    global vertex
    timer += 1
    dfn[u] = timer
    low[u] = timer
    son = 0
    flag = False
    for i in range(len(edge[u])):
        v = edge[u][i]
        if v == father:
            continue
        if not dfn[v]:
            son += 1
            dfs(v, u)
            if dfn[u] <= low[v]:
                flag = True
            low[u] = min(low[u], low[v])
        else:
            low[u] = min(low[u], dfn[v])
    if (not father and son > 1) or (father and flag):
        cut.append(u)

def tarjan():
    global vertex
    for i in range(vertex):
        if not dfn[i + 1]:
            dfs(i + 1, 0)

if __name__ == "__main__":
    vertex, size = map(int, input().split())
    edge = []
    for i in range(vertex + 1):
        edge.append([])
    dfn = [0] * (vertex + 1)
    low = [0] * (vertex + 1)
    while size:
        u, v = map(int, input().split())
        edge[u].append(v)
        edge[v].append(u)
        size -= 1
    timer = 0
    cut = []
    tarjan()
    print(cut)