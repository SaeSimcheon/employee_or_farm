import sys
sys.stdin = open("cht3_8_input.txt","rt")

indicator = int(input())
matrix = list()

for i in range(indicator):
    matrix.append(list(map(int,input().split())))

nun_com = int(input())


com_matrix = list()

for i in range(nun_com):
    com_matrix.append(list(map(int,input().split())))

#print(matrix,com_matrix)


#1 rotation

for i in range(nun_com):
#    print(i)
    com = com_matrix[i]
    if com[2] >=indicator:
        com[2] = com[2] %indicator
    if com[1] ==0:
        back=matrix[com[0]-1][:com[2]]
        front=matrix[com[0]-1][com[2]:]
        
#        print(back)
#        print(front)
        front.extend(back)
        matrix[com[0]-1] = front
    else:
        back=matrix[com[0]-1][:(indicator-com[2])]
        front=matrix[com[0]-1][(indicator-com[2]):]
        front.extend(back)
        matrix[com[0]-1] = front

# rotation 횟수만큼 반복문을 수행
# 회전 좌우에 따라 조건문을 따로 수행하는데
# 왼쪽으로 수행하는 경우 회전수까지를 해당 행에서 앞에서부터 잘라 뒤에 붙였음.
# 오른쪽의 경우 자르는 기준을 뒤에서부터 셀 수 있도록 indicator 즉, 행의 크기에서 뺌
# matrix에서 해당 행을 반복해서 대체
# 단 회전수가 행의 크기보다 큰 경우에는 행의 크기로 나눈 나머지로 수행   

        
#2 Hourglass

med=(indicator+1)/2-1 

all_sum = 0
left = 0
right = int(indicator)

for i in range(indicator):
#    print(left,right)
    if i <med:
        all_sum += sum(matrix[i][left:right])
        left +=1
        right -=1
#        print(all_sum)
    else :
        all_sum += sum(matrix[i][left:right])
        left -=1
        right +=1
    
print(all_sum)

# 앞서 7번의 풀이를 역으로 이용
# 늘이다 줄이는 방식을 줄이다 늘이는 방식으로 변경.