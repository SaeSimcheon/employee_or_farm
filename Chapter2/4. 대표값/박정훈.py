import sys

#sys.stdin=open('input.txt','rt')

N = int(input())
score = list(map(int, input().split()))
ave = sum(score)/int(N)
ave = round(ave)
score_minus_average = list(x - ave for x in score)

diff = list(map(abs, score_minus_average)) #절대값이 가장 작은 값으로

diff_set = set(diff)

if len(diff) == len(diff_set): #동점자가 없을 때
    index = diff.index(min(diff))
    print(score[index], index)
else :
    min_value = 2147000000
    mean_value = 2147000000
    index_candidate = int()
    for i in range(len(score)): #최솟값 update
        if min_value > diff[i]:
            min_value = diff[i]
            mean_value = score[i]
            index_candidate = i+1
        elif min_value == diff[i]: #동점자가 있을 때 더 큰 점수 혹은 빠른 index
            if score[index_candidate-1] - score[i] >0 : # index_candidate가 더 큰 점수
                mean_value = score[index_candidate-1]
                index_candidate = index_candidate
            elif score[index_candidate-1]==score[i] : # 같은 점수면 이전 candidate
                index_candidate = index_candidate
                mean_value = score[index_candidate-1]
            elif score[index_candidate-1] < score[i] : #새로운게 더 큰 점수
                mean_value = score[i]
                index_candidate = i+1
    print(ave, index_candidate)
#100점

'''
n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/n)
min = 2147000000
for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp<min:
        min=tmp
        score = x
        res = idx+1
    elif tmp==min:
        if x>score:
            score = x
            res = idx+1
print(ave, res)
'''




