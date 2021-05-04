import sys

#sys.stdin=open('input.txt','rt')
'''
ans = ''

def DFS(x):
    global ans
    length = 0
    while x - 2 ** length > 0:
        length += 1
    for i in range(length):
        if x // 2**(length-i) >0 :
            ans = ans + '1'
            DFS(x-2**(length-i))
        elif x // 2**(length-i) ==0:
            ans = ans + '0'
            DFS(x - 2**(length-i)

'''

def DFS(x):
    if x == 0 :
        return
    else:
        DFS(x//2)
        print(x%2, end='')

if __name__=='__main__':
    n=int(input())
    DFS(n)
