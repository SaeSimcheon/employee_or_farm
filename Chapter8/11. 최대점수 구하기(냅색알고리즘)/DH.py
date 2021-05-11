'''
최대점수 구하기(냅색 알고리즘)

시간 대비 가성비 좋은 점수로 sort(내림차순)
'''


n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
'''
n,m = 5,20
arr = [[10,5],[25,12],[15,8],[6,3],[7,4]] # 점수 시간
'''
arr.sort(key = lambda x:(-x[0]/x[1]))

dy = [arr[0]]
ans = -2
for ls in arr[1:]:
    tmp_max = -1
    tmp_ls = []
    for j in dy:
        if j[1] + ls[1] <= m and tmp_max < j[0]:
            tmp_max = j[0]
            tmp_ls = [j[0] + ls[0],j[1] + ls[1]]
    dy.append(tmp_ls)
    if ans < tmp_ls[0]:
        ans = tmp_ls[0]

print(ans)
