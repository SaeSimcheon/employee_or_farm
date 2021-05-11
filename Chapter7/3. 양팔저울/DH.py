'''
양팔저울

All : 모든 조합의 수

b : (그릇 + 추) : 추 >> 그릇 : 추 - 추 [All에서 2개씩 뽑는 것]

0이 b에 있으면 +1


'''

import sys
'''
from itertools import combinations
#sys.stdin = open("in1.txt","r")


k = int(input())
arr = list(map(int,input().split()))
#print(arr)


S = sum(arr)

All = []
for i in range(1,k+1):
    ls = list(combinations(arr,i))
    All += [sum(x) for x in ls]

b = list(combinations(All,2)) 
b = [abs(x-y) for x,y in b]+ All
b = list(set(b))

if 0 in b:
    print(S-len(b)+1)
else:
    print(S-len(b))

'''


'''
DFS
'''

k = int(input())
arr = list(map(int,input().split()))

S = sum(arr)

ALL = []

def DFS(li,num):
    global ALL
    if len(li) == 0:
        ALL += [num]
        return

    else:
        DFS(li[1:],num + li[0])
        DFS(li[1:],num)
        DFS(li[1:],num - li[0])
DFS(arr,0)
ALL = [x for x in set(list(ALL)) if x >0]

print(S - len(ALL))
