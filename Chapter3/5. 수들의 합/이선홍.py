import sys
#sys.stdin=open("c:/Users/jung/Desktop/AA/in2.txt","r")
n,m=map(int,input().split())
base=list(map(int,input().split()))
case_num=0

for i in range(n):
    for j in range(i,n):
        if sum(base[i:j+1])==m:
            case_num+=1

print(case_num)

## time limit exceeded
