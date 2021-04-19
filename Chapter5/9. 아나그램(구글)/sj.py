import sys
#sys.stdin = open("input.txt", "rt")
'''a = input()
b = input()
if sorted(a) == sorted(b):
    print("YES")
else:
    print("NO")'''

# dictionary로도 풀어보자
'''a = input()
b = input()
w1 = dict()
w2 = dict()
for i in a:
    if i in w1:
        w1[i] += 1
    else:
        w1[i] = 1
for j in b:
    if j in w2:
        w2[j] += 1
    else:
        w2[j] = 1
if w1 == w2:
    print("YES")
else:
    print("NO")'''

# 둘다 100

'''a = input()
b = input()
str1 = dict()
str2 = dict()
for x in a:
    str1[x] = str1.get(x,0)+1
for x in b:
    str2[x] = str2.get(x,0)+1

for i in str1.keys():
    if i in str2.keys():
        if str1[i]!=str2[i]: # 같은 key의 value가 다를때
            print("NO")
            break
    else: # key가 다를떄
        print("NO")
        break
else:
    print("YES")
# 비교 방법이 너무 복잡해서, 개선한 코드
a = input()
b = input()
sH = dict()
for x in a:
    sH[x] = sH.get(x,0)+1
for x in b:
    sH[x] = sH.get(x,0)-1
for x in a:
    if sH.get(x)>0:
        print("NO")
        break
else:
    print("YES")'''

# 리스트 버전 / 아스키 넘버 이용
# 대문자는 65~90(64를 뺴기) / 소문자는 97~(71를 빼기)
a = input()
b = input()
str1 = [0]*52
str2 = [0]*52
for x in a:
    if x.isupper():
        str1[ord(x)-65]+=1
    else:
        str1[ord(x)-71]+=1
for x in b:
    if x.isupper():
        str2[ord(x)-65]+=1
    else:
        str2[ord(x)-71]+=1
for i in range(52):
    if str1[i]!=str2[i]:
        print("NO")
        break
else:
    print("YES")

# 느낀점
# 1. 해싱 조건이 좀 까다롭다

# 배운점
# 1. dict.get(x,0) : key x의 value를 호출하고 없으면 0을 호출
# 2. 아스키 넘버 사용
# 3. 리스트나 딕셔너리간의 직접 비교는 지양 / c++ 처럼 하나하나 비교하는 식으로 코딩해야함함