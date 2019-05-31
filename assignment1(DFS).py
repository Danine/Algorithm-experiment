def DFS(u):
    global edge
    edge[u][0] = 1
    i = 1
    while i < len(edge[u]):
        if edge[edge[u][i]][0] == 0:
            DFS(edge[u][i])
        elif edge[edge[u][i]][0] == 1:
            edge[u][i] = 0
        i += 1
    edge[u][0] = 2

if __name__ == "__main__":
    vertex, size = map(int, input().split())#?????????
    edge = []
    for i in range(vertex + 1):
        edge.append([0])
    for j in range(size):
        u, v = map(int, input().split())
        edge[u].append(v)
    for i in range(1,vertex + 1):
        if edge[i][0] == 0:
            DFS(i)
    m = 1
    for n in range(1,len(edge)):
        edge[n].pop(0)
        print(str(m) + ':' + str(edge[n]))
        m += 1

'''
6 7
1 2
3 1
3 2
2 4
4 3
5 4
5 6
'''