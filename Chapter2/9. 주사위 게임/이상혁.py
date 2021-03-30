import sys
sys.stdin = open("cht2_9_input.txt","rt")

n=int(input())

people = list()
for i in range(n):
    one_man=list(map(int,input().split()))
    people.append(one_man)
    

def prize(one):
    counting=[one.count(1),one.count(2),one.count(3),one.count(4),one.count(5),one.count(6)]
    if 3 in counting:
        return 10000 + 1000*(counting.index(3)+1)
    elif 2 in counting :
        return 1000 + 100*(counting.index(2) + 1 )
    else :
        return (max([idx for idx,value in enumerate(counting) if value != 0])+1)*100
    

print(max(list(map(prize,people))))