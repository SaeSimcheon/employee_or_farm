import sys
#sys.stdin=open('in1.txt','r')
def recur(n,z):
    if z>=0:
        if n>=2**z:
            print(1,end='')
            n-=2**z
        else:
            print(0,end='')
        z-=1
        recur(n,z)
        
n=int(sys.stdin.readline())
z=0
while n>=2**(z+1):
    z+=1

recur(n,z)
