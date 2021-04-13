import sys
#sys.stdin=open("in3.txt","r")
n=int(input())
base=list(map(int,input().split()))

a1=[]
a2=''
while len(base)>0:
    lt=base[0]
    rt=base[-1]
    if len(base)==n: ## 맨처음에
        if lt<rt:
            a1.append(lt)
            a2+='L'
            base=base[1:]
        else:
            a1.append(rt)
            a2+='R'
            base=base[:-1]
    
        continue
    
    if len(base)==1 and lt>a1[-1]:
        a1.append(lt)
        a2+='L'
        break

    if lt>a1[-1]:
        a1.append(lt)
        a2+='L'
        base=base[1:]
    elif rt>a1[-1]:
        a1.append(rt)
        a2+='R'
        base=base[:-1]
    else:
        break
        
print(len(a1))
print(a2)