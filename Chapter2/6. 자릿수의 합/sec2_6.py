Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
>>> sys.stdin=open("c:/Users/jung/Desktop/AA/in5.txt","r")
>>> n=int(input())
>>> data=list(map(int,input().split()))
>>> def digit_sum(x):
	sx=str(x)
	sum=0
	for i in sx:
		sum+=int(i)
	return(sum)

>>> m=list()
>>> max=0
>>> for i,x in enumerate(data):
	m.append(digit_sum(x))

>>> idx=0
>>> for i,x in enumerate(m):
	if x>max:
		max=x
		idx=i

		
>>> print(x,i)
20 99
>>> 