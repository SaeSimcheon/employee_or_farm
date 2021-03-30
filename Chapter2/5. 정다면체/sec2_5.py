Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
>>> sys.stdin=open("c:/Users/jung/Desktop/AA/in3.txt","r")
>>> n, m=map(int, input().split())
>>> cnt=[0]*(n+m)
>>> max=0
>>> max
0
>>> for i in range(1, n+1):
	    for j in range(1, m+1):
		cnt[i+j]=cnt[i+j]+1
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for i in range(1,n+1):
	for j in range(1,m+1):
		cnt[i+j]=cnt[i+j]+1

Traceback (most recent call last):
  File "<pyshell#11>", line 3, in <module>
    cnt[i+j]=cnt[i+j]+1
IndexError: list index out of range
>>> cnt=[0]*(n+m+1)
>>> for i in range(1,n+1):
	for j in range(1,m+1):
		cnt[i+j]=cnt[i+j]+1

>>> for i in range(n+m+1):
	if cnt[i]>max:
		max=cnt[i]

>>> max
12
>>> for i in range(n+m+1):
	if cnt[i]==max:
		print(i)

13
14
15
16
17
18
19
20
21
>>> 