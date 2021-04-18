import sys
#sys.stdin = open("input.txt", "rt")

##### 해쉬 자료구조 활용 #####

n = int(input())
p = dict()

for i in range(n):
    word = input()
    p[word] = 1
#print(p)

for i in range(n-1):
    word = input()
    p[word] = 0
#print(p)

for key, val in p.items():
    if val == 1:
        print(key)
        break

'''
n = int(input())
words = []
for _ in range(n):
    a = input()
    words.append(a)

words2 = []
for _ in range(n-1):
    b = input()
    words2.append(b)

for x in words:
    if x not in words2:
        print(x)

'''