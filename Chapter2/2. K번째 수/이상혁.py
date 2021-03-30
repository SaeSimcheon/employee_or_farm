
import sys
#sys.stdin = open("input.txt","rt")

n= int(input(""))
for i in range(n):
    parameters = list(map(int,input("").split()))
    seq = list(map(int,input("").split()))
    selected = seq[parameters[1]-1:parameters[2]]
    selected.sort()
    print("#"+str(i+1),selected[parameters[3]-1])
    
