import sys
sys.stdin=open("input.txt", "r")

N = int(input())
seq = list()
for i in range(N):
    tt=list(input().split())
    tt=list(map(int,list(*tt)))
    seq.append(tt)


print(seq)






