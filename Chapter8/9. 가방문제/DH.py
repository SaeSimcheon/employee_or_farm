'''
가방문제(냅색 알고리즘)

'''
import sys
#sys.stdin = open("in1.txt")
n,l = map(int,input().split())

dic = {}

for _ in range(n):
    k,v = map(int,input().split())
    dic[k] = v

'''
n,l = 4,11
dic = {4:8,5:12,3:8,6:14}
'''

dy = [0] * (l+1)


for i in range(1,l+1):

    post = [[i - x,x] for x in dic.keys() if i - x >= 0]
        
    if len(post) == 0:
        continue
    else:
        post = [dy[x[0]] + dic[x[1]] for x in post]

        dy[i] = max(post)

print(dy[-1])

