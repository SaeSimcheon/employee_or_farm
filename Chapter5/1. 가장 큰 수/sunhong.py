import sys
#sys.stdin=open('in5.txt','r')
base,m=map(int,sys.stdin.readline().split())
base=[int(x) for x in str(base)]
stack=[]

stack.append(base[0])
cnt=0
idx=0
for i in range(1,len(base)):
    idx=i
    if base[i]<=stack[-1]:
        stack.append(base[i])
    else:
        while base[i]>stack[-1] :
            stack.pop()
            cnt+=1
            if cnt==m:
                break
            if len(stack)==0:
                break
        stack.append(base[i])
    if cnt==m:
        break
    if len(stack)==len(base)-m:
        break


if len(stack)>len(base)-m:
    stack=stack[:-cnt+m]
    for x in stack:
        print(x,end='')
elif len(stack)==len(base)-m:
    for x in stack:
        print(x,end='')
else :
    stack+=base[idx+1:]
    for x in stack:
        print(x,end='')


#### 노가다코드, time limit exceeded ####
import sys
import itertools
#sys.stdin=open("in1.txt","r")
data,m=map(int,sys.stdin.readline().split())
d=str(data)
a=list(range(len(d)))

max=0
for x in list(itertools.combinations(a,len(d)-m)):
    f=''
    for index in x:
        f+=d[index]
    if int(f)>max:
        max=int(f)
        
print(max)

## len(number)-m 개를 선택하는 모든 조합을 고려해서 최대값찾음
## case 2,3 time lime exceeded, 60점