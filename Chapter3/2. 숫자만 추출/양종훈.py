import sys
#sys.stdin = open("input.txt", "rt")

s = input()

res = 0
for x in s:
    if x.isdecimal():
        res = res*10 + int(x)
print(res)

cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)



'''
word = input()
num = 0

for i in range(len(word)):
    if word[i].isdigit():
        num = num * 10 + int(word[i])

cnt = 1
for n in range(2, num + 1):
    if num % n == 0:
        cnt += 1

print(num)
print(cnt)
'''