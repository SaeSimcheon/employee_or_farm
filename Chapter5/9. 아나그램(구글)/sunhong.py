import sys
from collections import Counter
#sys.stdin=open("in1.txt"."r")
a=map(str,sys.stdin.readline())
b=map(str,sys.stdin.readline())
if Counter(a)==Counter(b):
    print("YES")
else:
    print("NO")
