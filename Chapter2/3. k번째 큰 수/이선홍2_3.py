Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
>>> sys.stdin=open("c:/Users/jung/Desktop/AA/in2.txt","r")
>>> n,k=map(int,input().split())
>>> data=list(map(int,input().split()))
>>> l=list()
>>> for i in range(n):
	for j in range(i+1,n):
		for k in range(j+1,n):
			l.append(data[i]+data[j]+data[k])

\
>>> l.sort(reverse=True)
>>> print(l[k[)
	
SyntaxError: invalid syntax
>>> print(l[k])
149
>>> 