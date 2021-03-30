'''
대표값

'''
import sys

#sys.stdin = open("in1.txt","rt")


n = int(input())
L = list(map(int,input().split()))


AVG = round(sum(L)/n)
L = [[idx+1,x - AVG] if x - AVG >= 0 else [idx+1,abs(x-AVG)+0.5] for idx,x in enumerate(L) ]
L = sorted(L,key = lambda x: (x[1],x[0]))
print(AVG,L[0][0],sep = " ")
