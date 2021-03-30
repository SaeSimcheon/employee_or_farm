Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> sys.stdin=open("c:/Users/jung/Desktop/AA/in2.txt","r")
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    sys.stdin=open("c:/Users/jung/Desktop/AA/in2.txt","r")
NameError: name 'sys' is not defined
>>> import sys
>>> sys.stdin=open("c:/Users/jung/Desktop/AA/in2.txt","r")
>>> n=int(input())
>>> score=list(map(int,input().split()))
>>> mat_mean=round(sum(score)/len(score),1)
>>> min_val=float('inf')
>>> min_val
inf
>>> for i,x in enumerate(score):
	abs_val=abs(x-mat_mean)
	if abs_val<min_val:
		min_val=abs_val
		mat_score=x
		ind=i+1
	elif abs_val==min_val:
		if x> mat_score:
			mat_score=x
			ind=i+1

>>> print(min_val,mat_score,ind)
1.0 34 2
>>> 