import sys
sys.stdin = open("input.txt","rt")

N = int(input())
seq =list(map(int,input().split()))

ch = [0]*(N+1)
seq.insert(0,0)
ch[1]=1
out = 0

for i in range(2,N+1):
    maximum = 0
    for j in range(i-1,0,-1):
        #print(i,j)
        if seq[i] > seq[j] and ch[j] > maximum:
            maximum = ch[j]
        
    ch[i] = maximum +1
    
print(max(ch))


#print(list(range(1,0,-1)))