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

>>> p=list()
>>> n=20
>>> for i in range(2,n+1):
	if isPrime(i)==True:
		p.append(i)

>>> 