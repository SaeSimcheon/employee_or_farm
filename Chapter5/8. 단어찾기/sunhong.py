import sys
#sys.stdin=open("in1.txt","r")
n=int(sys.stdin.readline())
note=[]
for _ in range(n):
    note+=sys.stdin.readline().split()
poet=[]
for _ in range(n-1):
    poet+=sys.stdin.readline().split()

for x in note:
    if x not in poet:
        print(x)
        break

## 이거 dictionary형태로 풀어보기
