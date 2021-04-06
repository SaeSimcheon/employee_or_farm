import sys
sys.stdin = open("cht3_10_input.txt","rt")

matrix = list()
for i in range(9):
    matrix.append(list(map(int,input().split())))

def checker(element):
    if len(set(element)) ==9:
        return "YES"
    else:
        return "NO"

boxer = list()
for k in range(3):
    for l in range(3):
        boxer.append([matrix[i][j] for i in range(9) for j in range(9) if (i //3 == k)&(j //3 == l)])

            
row = list(map(checker,matrix))
col = list(map(checker,zip(*matrix)))
box = list(map(checker,boxer))

if ("NO" in row)|("NO" in col)|("NO" in box):
    print("NO")
else :
    print("YES")