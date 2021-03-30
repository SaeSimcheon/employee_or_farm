import sys
#sys.stdin=open("input.txt", "rt")

n, k = map(int, input().split())
cnt=0
for i in range(1,n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)



'''
1. 데이터 불러오는 거부터 모름
2. if/break 활용
3. for에도 else가 있더라
'''
