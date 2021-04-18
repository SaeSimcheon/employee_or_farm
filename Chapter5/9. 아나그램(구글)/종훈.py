import sys
#sys.stdin = open("input.txt", "rt")

##### 해쉬 자료구조 활용 #####

### dict.get("A", 0) : dictionary 안에 A라는 key가 없으면 0을 return, 있으면 대응하는 value를 return

#### CASE3 : list hash
# 아스키 넘버 이용

a = input()
b = input()
str1 = [0] * 52
str2 = [0] * 52

for x in a:
    if x.isupper(): # isupper() : 대문자인지 알려주는 함수
        str1[ord(x) - 65] += 1 # ord : 문자를 아스키넘버로 바꿔주는 함수
    else:
        str1[ord(x) - 71] += 1
        # 대문자는 65 ~ 90, 소문자는 97 ~ 122 각각 26개로 str칸을 52개로

for x in b:
    if x.isupper(): 
        str2[ord(x) - 65] += 1 
    else:
        str2[ord(x) - 71] += 1

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")


#### CASE2

a = input()
b = input()
sH = dict()

for x in a:
    sH[x] = sH.get(x, 0) + 1
for x in b:
    sH[x] = sH.get(x, 0) - 1

for x in a:
    if sH.get(x) > 0:
        print("NO")
        break
else:
    print("YES")

#### CASE 1

a = input()
b = input()
str1 = dict()
str2 = dict()

for x in a:
    str1[x] = str1.get(x, 0) + 1
for x in b:
    str2[x] = str2.get(x, 0) + 1

for i in str1.keys():
    if i in str2.keys(): # 아나그램의 전제조건으로 str1에 있는 key가 str2에도 존재해야 한다.
        if str1[i] != str2[i]: # 숫자가 다르면 break
            print("NO")
            break
    else: # 존재하지 않으면 바로 break
        print("NO")
        break
else:
    print("YES")


'''
p = dict()
word = input()
for x in list(set(word)):
    p[x] = 0
#print(p)

for x in word:
    p[x] += 1

word2 = input()
for x in word2:
    p[x] -= 1

for key, val in p.items():
    if val != 0:
        print("NO")
        break
else:
    print("YES")
'''