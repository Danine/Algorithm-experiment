'''
求最小TSP圈
'''
def TSP(c, now):
    global last, stack, small, road, current
    temp = c.copy()
    stack.append([now, edge[last][now]])
    current += edge[last][now]
    if current >= small:
        current -= edge[last][now]
        stack.pop()
        return
    del temp[temp.index(now)]
    if temp == []:
        w = 0; r = ''
        stack.append([stack[0][0],edge[now][stack[0][0]]])
        for i in stack:
            w += i[1]
            r = r + '->' + str(i[0])
        stack.pop()
        if w < small:
            small = w
            road = r
    else:
        last = now
        for i in temp:
            TSP(temp, i)
    tp = stack.pop()
    if stack == []:
        pass
    else:
        current -= tp[1]
        last = stack[-1][0]


if __name__ == "__main__":
    vertex = int(input())
    edge = []
    for i in range(vertex + 1):
        edge.append([0])
    for i in range(vertex):
        edge[0].append(0)
    for i in range(1, vertex + 1):
        temp = map(int, input().split())
        edge[i] += temp
    tag = []
    for i in range(1, vertex + 1):
        tag.append(i)
    stack = []
    small = 10000
    current = 0
    road = ''
    last = 0
    cpt = tag.copy()
    TSP(cpt,1)
    print(road,small)

'''
4
0 1 6 15
2 0 9 8
5 3 0 3
4 7 2 0

4
0 3 6 7 
5 0 2 3 
6 4 0 2 
3 7 5 0

'''