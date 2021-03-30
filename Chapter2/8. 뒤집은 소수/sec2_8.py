Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def isPrime(x):
	if x==1:
		print("1is not prime num")
	re=True
	for i in range(2,x):
		if x%i==0:
			re=False
			break
		else:
			re=True
	return re

>>> def rev(x):
	x=str(x)
	xx='0'
	for i in range(len(x)):
		xx+=x[len(x)-1-i]
	xx=int(xx)
	return xx

>>> rev_dat=list()
>>> for i in range(n):
	rev_dat.append(rev(i))

	
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    for i in range(n):
NameError: name 'n' is not defined
>>> for i,x in enumerate(rev_dat):
	if isPrime(x)==True:
		print(x)
