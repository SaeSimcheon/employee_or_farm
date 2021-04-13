import sys
#sys.stdin=open("in2.txt","r")
n=int(input())
base=[list(map(int,input().split())) for _ in range(n)]
base.sort()

def find_min_endt(data):
    m=9**8
    for x in data:
        if x[1]<m:
            m=x[1]
    return m

def ff(base):
    for i,x in enumerate(base):
        if x[0]>=find_min_endt(base): ## 현재 주어진 데이터에서, 가장 빠른 종료시간을 찾고, 시작시간이 그 이후인 데이터만 남김
            new_base=base[i:] ## base는 이미 시작시간을 기준으로 sort된 상태
            break
    return new_base

maxx=base[-1][-1]
cnt=1
while True:
    cnt+=1
    base=ff(base) 
    if base[0][-1]+1>maxx:
        break    
print(cnt)
