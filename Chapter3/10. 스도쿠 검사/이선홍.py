import sys
#sys.stdin=open("c:/Users/jung/Desktop/AA/in1.txt","rt")
base=[list(map(int,input().split())) for _ in range(9)]
base_t=list(map(list, zip(*base)))
a1=[]
a2=[]
a3=[]
a4=[]
a5=[]
a6=[]
a7=[]
a8=[]
a9=[]
for i,x in enumerate(base):
    if i<3:
        a1.extend(x[slice(0,3)])
        a2.extend(x[slice(3,6)])
        a3.extend(x[slice(6,9)])
    elif i<6:
        a4.extend(x[slice(0,3)])
        a5.extend(x[slice(3,6)])
        a6.extend(x[slice(6,9)])
    else:
        a7.extend(x[slice(0,3)])
        a8.extend(x[slice(3,6)])
        a9.extend(x[slice(6,9)])

a=[a1,a2,a3,a4,a5,a6,a7,a8,a9]


def sudoku(d):
    s=0
    sbal=list(range(1,10))
    for x in d:
    	if list(set(x))==sbal:
    		s+=1
    return s

if sudoku(a)+sudoku(base)+sudoku(base_t)==27:
    print("YES")
else:
    print("NO")
