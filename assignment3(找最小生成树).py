'''
求解最小生成树
从T=空集开始
for(每条边e)
    if 加入e不构成环，
        T = T + e
    else
        e'是环上权重最大的边
            T = T + e - e'
思路：删除叶节点剩下环，删除环上最大的边
'''
import copy
def find():
    global edge,cp
    flag = True
    while flag:
        maxi = 0; maxj = 0; temp = 0
        i = 1
        m = 1
        while m < len(cp):
            if len(cp[m]) == 1:
                del cp[cp[m][0][0]][cp[cp[m][0][0]].index([m,cp[m][0][1]])]
                cp[m] = []
                m = 1
            else:
                m += 1
        null = True
        for x in cp:
            if x != []:
                null = False
                break
        if null == True:
            flag = False
            break
        else:
            while i < len(cp):
                for j in range(len(cp[i])):
                    if cp[i][j][1] > temp:
                        maxi = i; maxj = j
                        temp = cp[i][j][1]
                i += 1
            if maxi:
                duiying = cp[maxi][maxj][0]
                del edge[maxi][edge[maxi].index([duiying,temp])]
                del edge[duiying][edge[duiying].index([maxi,temp])]
                del cp[maxi][maxj]
                del cp[duiying][cp[duiying].index([maxi,temp])]
                cp = copy.deepcopy(edge)


if __name__ == "__main__":
    vertex, size = map(int, input().split())
    edge = []
    for i in range(vertex + 1):
        edge.append([])
    for i in range(size):
        u, v, l = map(int, input().split())
        edge[u].append([v,l])
        edge[v].append([u,l])
    cp = copy.deepcopy(edge)
    find()
    q = 1
    for p in edge[1:]:
        print(str(q)+':'+str(p))
        q += 1

'''
6 10
1 2 6
1 3 1
1 4 5
2 3 5
3 4 5
2 5 3
3 5 6
3 6 4
4 6 2
5 6 6
'1': '3', 
'2':'3', '5', 
'3': '1','2','6',
'4':'6', 
'5':'2', 
'6':'3','4'
'''