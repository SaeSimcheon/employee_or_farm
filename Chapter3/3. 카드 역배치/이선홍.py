import sys
#sys.stdin=open("c:/Users/jung/Desktop/AA/in1.txt","r")
base=list(range(1,21))
for _ in range(10): ## 이하구문과 상관없는 x같은 변수를 써도 되지만 _가 변수지정을 하지 않음으로 가장 빠름
    s,e=map(int,input().split())
    prac=base[s-1:e]
    base[s-1:e]=prac[::-1]

for x in base:
    print(x, end=' ')
