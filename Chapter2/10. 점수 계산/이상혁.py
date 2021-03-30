import sys
sys.stdin = open("cht2_10_input.txt","rt")

n=int(input())

seq=list(map(int,input().split()))
summ = 0
weighted = list()
for i in range(n):
    sliced=seq.pop(0)
    if  sliced != 0:
        summ += 1
        weighted.extend([summ])
    else :
        summ = 0
        weighted.extend([summ])
print(seq)
print(weighted)
