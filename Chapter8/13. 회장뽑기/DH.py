'''
회장뽑기(플로이드-워샬 응용)
'''

n = int(input())
dic = {i:[]for i in range(1,n+1)}
while 1:
    s,e = map(int,input().split())
    if [s,e] == [-1,-1]:
        break
    else:
        dic[s].append(e)
        dic[e].append(s)


'''

n = 5
arr = [[1,2],[2,3],[3,4],[4,5],[2,4],[5,3]]
dic = {i:[]for i in range(1,n+1)}
for x,y in arr:
    dic[x].append(y)
    dic[y].append(x)
'''


#ans = [[0] * n for i in range(n)]
min_ = 222222
ANS = []
for num in range(1,n+1):
    visit = [num]
    ls = [[num],0]

    while 1:
        q,cnt = ls
        post = []

        for i in q:
            tmp = [x for x in dic[i] if x not in visit]
            post += tmp
            visit += tmp
        if len(post) == 0:
            break
        else:
#            for i in post:
#                ans[num-1][i-1] = cnt +1
            ls = [post,cnt+1]
    if cnt <= min_:
        if cnt < min_:
            min_ = cnt
            ANS = []
        ANS.append(num)
print(min_,len(ANS),sep = " ")
for i in ANS:
    print(i,end = " ")

