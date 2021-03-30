Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
>>> sys.stdin=open("c:/Users/jung/Desktop/AA/in1.txt","r")
>>> t=int(input())
>>> t
2
>>> for i in range(t):
	n,s,e,k=map(int,input().split())
	dat=[map(int,input().split())]
	dat=dat[s-1:e]
	dat.sort()
	print(dat[k-1)
	      
SyntaxError: invalid syntax
>>> for i in range(t):
	n,s,e,k=map(int,input().split())
	dat=[map(int,input().split())]
	dat=dat[s-1:e]
	dat.sort()
	print(dat[k-1])

Traceback (most recent call last):
  File "<pyshell#11>", line 6, in <module>
    print(dat[k-1])
IndexError: list index out of range
>>> import sys
>>> sys.stdin=open("c:/Users/jung/Desktop/AA/in1.txt","r")
>>> t=int(input())
>>> t
2
>>> for i in range(t):
	n,s,e,k=map(int,input().split())
	dat=[map(int,input().split())]
	dat=dat[s-1:e]
	dat.sort()
	print(dat[k-1])

Traceback (most recent call last):
  File "<pyshell#17>", line 6, in <module>
    print(dat[k-1])
IndexError: list index out of range
>>> sys.stdin=open("c:/Users/jung/Desktop/AA/in1.txt","r")
>>> t=int(input())
>>> t
2
>>> n,s,e,k=map(int,input().split())
>>> n
6
>>> s
2
>>> e
5
>>> k
3
>>> 
KeyboardInterrupt
>>> dat=[map(int,input().split())]
>>> dat
[<map object at 0x000001DDC8212488>]
>>> dat=dat[s-1:e]
>>> dat
[]
>>> sys.stdin=open("c:/Users/jung/Desktop/AA/in1.txt","r")
>>> t=int(input())
>>> n,s,e,k=map(int,input().split())
>>> dat=list(map(int,input().split()))
>>> dat
[5, 2, 7, 3, 8, 9]
>>> sys.stdin=open("c:/Users/jung/Desktop/AA/in1.txt","r")
>>> t=int(input())
>>> n,s,e,k=map(int,input().split())
>>> dat=list(map(int,input().split()))
>>> sys.stdin=open("c:/Users/jung/Desktop/AA/in1.txt","r")
>>> t=int(input())
>>> for i in range(t):
	n,s,e,k=map(int,input().split())
	dat=list(map(int,input().split()))
	dat=dat[s-1:e]
	dat.sort()
	print(dat[k-1])

7
584
>>> 