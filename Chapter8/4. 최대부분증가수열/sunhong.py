## 강의 설명보고 품
import sys
#sys.stdin=open('in1.txt','r')
n=int(sys.stdin.readline())
base=list(map(int,sys.stdin.readline().split()))

dy=[0]*n
dy[0]=1

for i in range(1,n):
    len=0
    for j in range(0,i):
        if base[i]>base[j]:
            len=max(len,dy[j]+1)
    dy[i]=max(1,len)
    
print(max(dy))

#### 20점짜리 막 푼거, 아예 틀림
def LIS(sample):
    a=[]
    for i in range(len(sample)):
        b=[]
        b.append(sample[i])
        for j in range(i+1,len(sample)):
            if b[-1]<sample[j]:
                b.append(sample[j])
#        print(b)
        a.append(len(b))
    return a

print(max(LIS(base)))

## 순열 조건에 맞다고해서 무조건 넣으면 안됨/ 최대길이 보장x 