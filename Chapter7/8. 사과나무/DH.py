'''
사과나무(BFS)
아쉽네
'''

import sys
#sys.stdin = open("in1.txt")
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
'''

n = 5
arr = [[10,13,10,12,15],
       [12,39,30,23,11],
       [11,25,50,53,15],
       [19,27,29,37,27],
       [19,13,30,13,19]]
'''
mid = n//2

start = [[0,mid]]
visit = [[0,mid],[n-1,mid]]
ans = 0

s,e = 0,n
while len(start) != 0:
    Temp = start.pop(0)
    if Temp[0] < mid:

        temp = [[Temp[0]+1,i] for i in range(Temp[1]-1,Temp[1]+2) if [Temp[0]+1,i] not in visit]
        start += temp
        visit += temp

        temp = [[n - Temp[0] - 2 ,i] for i in range(Temp[1]-1,Temp[1]+2) if [n - Temp[0] -2 ,i] not in visit]    
        start += temp
        visit += temp   
           
for i in visit:
    ans += arr[i[0]][i[1]]

print(ans)
