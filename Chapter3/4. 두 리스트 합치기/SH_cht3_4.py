import sys
sys.stdin = open("cht3_4_input.txt","rt")


n1 = int(input())
list1 = list(map(int,input().split()))
n2 = int(input())
list2 = list(map(int,input().split()))

list1.extend(list2)
list1.sort()
print(*list1)


# 중복을 없앨 필요도 없고 그냥 두 개 리스트 합칠 방법만 생각하면 됐었음.
# 1개 list를 확장하는 방법으로, 구체적으로 extend를 통하여 두 개 리스트를 하나로 만들어 주었고,
# sort로 정렬