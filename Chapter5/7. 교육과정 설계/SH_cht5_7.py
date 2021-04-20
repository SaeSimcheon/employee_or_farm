import sys
sys.stdin=open("input.txt", "r")
ans = input()
n=int(input())
seq= [input() for _ in range(n)]

ans=list(ans)
out = list()

for idx,element in enumerate(seq):
    que = list()
    for i in element:
        if i in ans:
            que.append(i)
        else: 
            continue
    if "".join(ans)=="".join(que):
        out.append("#{0} YES".format(idx+1))
    else:
        out.append("#{0} NO".format(idx+1))
        
print(*out,sep="\n")