import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    s = []
    for i in range(n):
        s.append(str(x[i]))

    b = []
    c = []
    for i in range(n):
        ss = 0
        for j in range(len(s[i])):
            ss += int(s[i][j])
        b.append(ss)
        c.append(s[i])
    return c[b.index(max(b))]

print(digit_sum(a))
