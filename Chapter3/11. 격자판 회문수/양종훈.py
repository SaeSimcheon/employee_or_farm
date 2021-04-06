import sys
#sys.stdin = open("input.txt", "rt")

a = [list(map(int, input().split())) for _ in range(9)]

def check(a):
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[i][j]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False

    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[a[i * 3 + k][j * 3 + s]] = 1
            if sum(ch3) != 9:
                return False
    return True

if check(a):
    print("YES")
else:
    print("NO")


'''
a = [list(map(int, input().split())) for _ in range(9)]

cnt = 0
for i in range(9):
    if list(set(a[i])) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        cnt += 1
    b = 0
    for j in range(9):
        b += a[j][i]
    if b != 45:
        cnt += 1

for l in [0, 3, 6]:
    for i in [0, 3, 6]:
        c = 0
        for j in range(3):
            for k in range(3):
                c += a[j+i][k+l]
        if c != 45:
            cnt += 1
    
if cnt == 0:
    print("YES")
else:
    print("NO")
'''