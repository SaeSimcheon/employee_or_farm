import sys
sys.stdin = open("cht3_7_input.txt","rt")

indicator = int(input())
matrix = list()

for i in range(indicator):
    matrix.append(list(map(int,input().split())))
    
med=(indicator+1)/2-1 
#median index
#print(med)
all_sum = 0
left = int(med)
right = int(med)
for i in range(indicator):
#    print(left,right)
    if i <med:
        all_sum += sum(matrix[i][left:right+1])
        left -=1
        right +=1
#        print(all_sum)
    else :
        all_sum += sum(matrix[i][left:right+1])
        left +=1
        right -=1
    
print(all_sum)

#indicator와 matrix 크기가 정방으로 같다는 점을 이용하였음
#각 행을 단위로 좌측과 우측의 index를 left right로 설정하여
#반복문이 수행될때마다 양옆에서 1씩 늘다가 median index (median -1)을 기준으로
#줄어들게해 대칭을 이루도록했음