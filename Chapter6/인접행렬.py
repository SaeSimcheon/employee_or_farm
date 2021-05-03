'''
인접행렬
'''

n,m = 6,9
ll = [[1,2,7],
      [1,3,4],
      [2,1,2],
      [2,3,5],
      [2,5,5],
      [3,4,5],
      [4,2,2],
      [4,5,5],
      [6,4,5]]


ans = [[0]*n for i in range(n)]

for i in ll:
    a,b,c = i

    ans[a-1][b-1] = c

for i in ans:
    for j in i:
        print(j,end = " ")
    print()
