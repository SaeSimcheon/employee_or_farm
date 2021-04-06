import sys

#sys.stdin=open('input.txt','rt')


'''
n=9
array = [list(map(int, input().split())) for _ in range(n)]

answer = [range(0:10)]
for i in rage(0,10):
    for j in rage(0,10):
        if array[i][j] = answer

for i in range(0,3):
    for j in range(0,3):
        center_x = i*3+1
        center_y = j*3+1
        box = [array[center_x-1][center_y-],
               array[center_x][center_y],
               array[center_x+1][center_y+1],
               array[center_x-1][center_y-1],
               array[center_x][center_y],
               array[center_x+1][center_y+1],
               array[center_x-1][center_y-1],
               array[center_x][center_y],
               array[center_x+1][center_y+1]]
        box = box.sort()
        if box = answer:
            answer = 1

'''
def check(a):
    for i in range(9):
        ch1 = [0]*10
        ch2 = [0]*10
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[i][j]]=1
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False
    for i in range(3):
        for j in range(3):
            ch3 = [0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
                if sum(ch3)!=9:
                    return False

    return True
a = [list(map(int,input().split())) for _ in range(9)]
if check(a):
    print('YES')
else:
    print('NO')
