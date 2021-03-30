import sys
sys.stdin = open("cht2_7_input.txt","rt")

n=int(input())

list_below_n=list(range(1,n+1))
caster = list()

while len(list_below_n) != 0 :
    divider=list_below_n.pop(0)
    if divider == 1 :
        pass
    else:
        list_below_n = [x for x in list_below_n if x % divider !=0]
        caster.extend([divider])
    
print(len(caster))