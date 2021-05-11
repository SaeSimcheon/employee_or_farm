import sys
sys.stdin=open("input.txt", "r")
N = int(input())


seq = [list(map(int,input().split())) for _  in range(N)]

out= 0 
for i in range(N//2+1):
    if i == N-i-1:
        out+= sum(seq[i][N//2-i:N//2+i+1])
    else:
        out+= sum(seq[i][N//2-i:N//2+i+1])
        out+= sum(seq[N-i-1][N//2-i:N//2+i+1])

print(out)