import sys
sys.stdin = open("input.txt", "rt")

li = []
for line in sys.stdin:
    li.append(list(map(int, line.split())))

num = li[0][0]
#print(num)
del li[0]

for i in range(num):
    a = li[i*2][1]
    b = li[i*2][2]
    k = li[i*2][3]
    #print(a)
    #print(b)
    #print(k)
    #print(sorted(li[i*2+1][a-1:b]))
    slist = sorted(li[i*2+1][a-1:b])
    #print(sorted)
    print(slist[k-1])
