import sys

sys.stdin = open("input.txt","rt")

N,C =map(int,input().split())

seq=list(str(N))
seq=list(map(int,seq))


# 높은 숫자일수록 좋은 것은 맞음
# 자리의 개수는 변하지 않으므로, 9로 시작해야 좋음
# 하지만 경우에 따라서는 작은 수도 나올 수 있다는 것을 생각해야함.
# 어디까지 절삭할 수 있을지 보는 방법?
# 최대 제거해야할 자리수까지 탐색하는 방법
# 5 / 5 2 일단 5가 최대 / 7을 만났으므로 5보다 7이 더 좋은 앞의 수이므로 5와 2를 절삭함

# container의 길이를 변화를 주며 활용할 것 / C의 여유분만큼

out=list()

while (C >0) :
    detector=seq[:C]
    locate=detector.index(max(detector))
    if  locate == 0:
        out.append(seq.pop(0))
    else:
        seq = seq[locate:]
        C = C - locate 
    if C == 1:
        #print(seq[seq.index(min(seq))])
        del seq[0]
        out.extend(seq)
        break
    if len(seq) == C :
        break
print("".join(map(str,out)))

