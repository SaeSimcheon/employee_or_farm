'''
부분집합 구하기(DFS)
'''
import sys
#sys.stdin = open("in1.txt","r")
n = int(input())

#n = 3

def DFS(ll,n):
    if ll[-1] > n:
        return

    else:
        for i in range(ll[-1]+1,n+1):
            DFS(ll+[i],n)
        for i in ll:
            print(i, end = " ")
        print()


for i in range(1,n+1):
    DFS([i],n)
