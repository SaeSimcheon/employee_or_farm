import sys
sys.stdin = open("cht3_2_input.txt","rt")

obj=list(input())
obj_=list(map(ord,obj))
obj_ = [obj[idx] for idx ,val in enumerate(obj_) if val <=57]


obj_="".join(obj_)
print(int(obj_))


check=[int(obj_) % i==0 for i in range(1,int(obj_)+1) ]
print(check)
print(sum(check))


# 아스키 코드를 활용하여 정수만 선택
# 이때, list comprehension과 enumerate사용
# int함수를 통한 int to string 에서 / 앞에 0이 오는 경우 무시하고 0이 아닌 수부터 시작
# 약수의 개수를 구하는 가장 좋은 방법은 무엇일까?