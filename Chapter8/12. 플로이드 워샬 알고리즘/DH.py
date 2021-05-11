'''
플로이드 워샬 알고리즘

플로이드 워샬 알고리즘을 사용했는 지는 모르겠음(100점 이긴함)

'''

from collections import deque
n,m = map(int,input().split())
dic = {i:{} for i in range(1,n+1)}
arr = []
for _ in range(m):
    s,e,v = map(int,input().split())
    arr.append([s,e,v])
    dic[s][e] = v   


'''
n,m = 5,8
arr = [[1,2,6],[1,3,3],[3,2,2],[2,4,1],[2,5,13],[3,4,5],[4,2,3],[4,5,7]]
dic = {i:{} for i in range(1,n+1)}
for i in arr:
    dic[i[0]][i[1]] = i[2]
'''

ans = {i:["M"] * n for i in range(1,n+1)}
      

def BFS(n):
    q = deque()
    q.append([n])
    r = [[n]]
    while 1:
        tmp = q.popleft()
        for i in arr:
            if i[0] == tmp[-1] and i[1] not in tmp:
                q.append(tmp + [i[1]])
                r += [tmp + [i[1]]]
        if len(q) == 0:
            break

    for i in r:
        if len(i) == 1:
            ans[i[0]][i[0]-1] = 0
        else:
            tmp = 0
            for num in range(1,len(i)):
                s,e = i[num-1],i[num]
                tmp += dic[s][e]

            if ans[i[0]][i[-1]-1] == "M" or ans[i[0]][i[-1]-1] > tmp:
                ans[i[0]][i[-1]-1] = tmp

for i in range(1,n+1):
    BFS(i)
for x in ans.values():
    for j in x:
        print(j,end = " ")
    print()

