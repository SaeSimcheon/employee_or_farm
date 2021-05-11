'''
송아지 찾기
'''

import sys
#sys.stdin = open("in1.txt","r")
s,e = map(int,input().split())
#print(s,e)

'''
s,e = 5,14
'''
l = e - s

if l < 0 :
    print(-1*l)
elif l == 0:
    print(0)
else:
    v,r = divmod(l,5)
    if r < 3:
        print(v+r)
    else:
        print(v+1+5-r)
