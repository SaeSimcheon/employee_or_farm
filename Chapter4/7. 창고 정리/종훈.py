import sys
#sys.stdin = open("input.txt", "rt")

L = int(input())
a = list(map(int, input().split()))
m = int(input())

a.sort()

for _ in range(m):
    a[0] += 1
    a[L-1] -= 1
    a.sort()
print(a[L-1] - a[0])

'''
l = int(input())
box = list(map(int, input().split()))
m = int(input())

box.sort(reverse = True)
#print(box)

for _ in range(m):
    box.sort(reverse = True)
    box[0] -= 1
    box[l-1] += 1

box.sort(reverse = True)
print(box[0]-box[l-1])
'''
