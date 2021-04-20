import sys
sys.stdin=open("input.txt", "r")

#seq=[int(input()) for i in range(10)]



hip = list()

while True:
    i = int(input())
    #print(i)
    if i not in [-1,0]:
        hip.append(i)
    elif i == -1 :
        break
    else :
        if len(hip) ==0:
            print(-1)
        else:
            print(min(hip))
            del hip[hip.index(min(hip))]
