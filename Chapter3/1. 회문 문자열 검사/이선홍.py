import sys
#sys.stdin=open("c:/Users/jung/Desktop/AA/in1.txt","rt")
n=int(input())
for i in range(n):
    x=input()
    if x.upper()==x[::-1].upper():
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
