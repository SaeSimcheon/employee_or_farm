import sys
from collections import deque
sys.stdin = open("input.txt","rt")

N = int(input())
seq =list(map(int,input().split()))


out = list()

out.append([seq[0]])



def ftn(subseq,given):
    if subseq[len(subseq)-1] < given : 
        result=[*subseq,given]
        return result
    else:
        return subseq
    
for i in range(1,N):
    mapped = list(map(lambda x : ftn(x,seq[i]),out))
    out.extend(mapped)
    out.append([seq[i]])
#    print(out)
    
#print(list(map(len,out)))
print(max(list(map(len,out))))