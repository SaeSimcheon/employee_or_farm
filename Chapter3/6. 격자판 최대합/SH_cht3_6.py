import sys
sys.stdin = open("cht3_6_input.txt","rt")

indicator = int(input())
matrix = list()

for i in range(indicator):
    matrix.append(list(map(int,input().split())))

row_sum=list(map(sum, matrix))
col_sum=list(map(sum,zip(*matrix)))


# row는 그대로 합을 구해도 됨
# col은 세로 단위로 원소를 쪼개서 합을 구한다고 생각했음
# two dimensional list를 *를 통해 낱낱으로 쪼갰고
# zip을 통하여 같은 자리에 있는 원소들을 묶음으로 보았음
# map은 이를 개별 element로 보고 합을 구하게됨

diag_sum = 0
inv_diag_sum = 0
for idx, part in enumerate(matrix):
    diag_sum+=part[idx]
    inv_diag_sum +=part[indicator-idx-1]

# 대각합과 역 대각합을 구하기 위하여 반복문을 사용하되,
# index를 통하여 대각과 역대각을 구할 것이므로, enumerate를 사용한다.
# enumerate를 two dimensional list에 적용한 경우 개별 행을 원소로 본다


print(max(max(row_sum),max(col_sum),diag_sum,inv_diag_sum))