'''
找一个负环
'''
def DFS(u):
    global edge, stack
    edge[u][0] = 1
    i = 1
    while i < len(edge[u]):
        stack.append(edge[u][i])
        if edge[edge[u][i][0]][0] == 0:
            DFS(edge[u][i][0])
        elif edge[edge[u][i][0]][0] == 1:
            virtual = stack.copy()
            n = virtual.pop()
            stack.pop()
            w = n[1]; r = str(n[0])
            n = virtual.pop()
            while n[0] != edge.index(edge[edge[u][i][0]]):
                w += n[1]
                r += '>-'+str(n[0])
                try:
                    n = virtual.pop()
                except:
                    break
            if w < 0:
                print(r[::-1])
        i += 1
    edge[u][0] = 0
    try:
        stack.pop()
    except:
        pass

if __name__ == "__main__":
    vertex, size = map(int, input().split())#点的个数，边的个数
    edge = []
    for i in range(vertex + 1):
        edge.append([0])
    for j in range(size):
        u, v, l = map(int, input().split())#起始点终止点及权重
        edge[u].append([v, l])
    stack = []
    DFS(1)


'''
5 10 
1 2 3
1 5 -4
1 3 8
2 1 -2
2 4 1
2 5 7
3 2 4
4 3 -5
4 1 2
5 4 6

5 6
1 2 1
2 3 1
3 4 1
4 5 1
5 1 1
3 5 -5
'''