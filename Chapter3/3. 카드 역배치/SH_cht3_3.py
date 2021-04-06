import sys
sys.stdin = open("cht3_3_input.txt","rt")

sorted_cards  = list(range(1,21))

for i in range(10):
    interval=list(map(int,input().split()))
    sliced=sorted_cards[(interval[0]-1):interval[1]][::-1]
    sorted_cards[(interval[0]-1):interval[1]] = sliced

    
print(*sorted_cards)

# 구간값을 통해서 slice한 것을 뒤집은 것을 sliced에 저장
# 이후 해당 부분에 대입