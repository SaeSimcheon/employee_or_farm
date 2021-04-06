import sys
#sys.stdin=open("c:/Users/jung/Desktop/AA/in2.txt","r")
n=int(input())
ln=list(map(int,input().split()))
m=int(input())
lm=list(map(int,input().split()))
ln+=lm
ln.sort()
for x in ln:
    print(x, end=" ")


##답지,sort는 nlogn 시간이 걸림, 이미 sort된 자료 사용할 때는 n만 걸리게 짤 수 있음
#p1=int(input())
#ln=list(map(int,input().split()))
#p2=int(input())
#lm=list(map(int,input().split()))
#c=[]
#i=j=0
#while i<p1 and j<p2:
#    if ln[i]<=lm[j]:
#        c.append(ln[i])
#        i+=1
#    else:
#        c.append(lm[j])
#        j+=1

#if p1<p2:
#    c=c+lm[j:]
#if p2<p1:
#    c=c+ln[i:]

#print(c)