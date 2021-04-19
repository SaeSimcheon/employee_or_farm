import sys
#sys.stdin = open("input.txt", "rt")
'''a = []
while True:
    try:
        b = int(input())
        if b != 0:
            a.append(b)
        elif b == 0:
            if a:
                print(min(a))
                a.clear()
            else:
                print(-1)
        elif b == -1:
            break
    except EOFError:
        break
'''
# 첫시도 0
# Time limit 4개에 exit code 1개,,,

# 문제 설명 그지같이 해놨네 자료구조 설명 안해놓으면 어떻게 푸냐;;
# 그냥 답없어서 강의본다

import heapq as hq
a=[]
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a)==0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)

# 배운점
# 1. heap 자료 구조형
# 힙 자료구조: 완전 이진 트리의 일종으로 우선순위 큐를 위해 만들어진 자료구조. 최댓값/최솟값을 빠르게 찾아낼 수 있도록 만들어졌다.
# 파이썬에서의 힙: import heapq를 통해 모듈을 가져올 수 있다.
# 다만 파이썬에서 제공하는 힙 모듈은 기본적으로 최소 힙 기능만을 동작한다.
# 또한 파이썬에서의 힙은 별개의 자료구조가 아닌 리스트를 힙으로써 다루기 때문에,
# 빈 리스트를 생성해서 heapq모듈의 함수를 호출할 때마다 리스트를 인자로 넘기는 구조이다.
# 일반적인 최대/최소값을 찾는 방법은 O(n) / heap을 이용하면 O(logn)
# heapq.heappush(lst, num): heappush()함수를 통해 원소를 추가하면 알아서 정렬해준다.
# heapq.heappop(lst): 가장 작은 원소(루트 노드)를 삭제 & 리턴 후 정렬한다.
# heapq.heapify(lst): 이미 원소가 들어있는 리스트를 힙으로 만들어 준다
# 참고 : https://www.daleseo.com/python-heapq/#%EC%B5%9C%EC%86%8C%EA%B0%92-%EC%82%AD%EC%A0%9C%ED%95%98%EC%A7%80-%EC%95%8A%EA%B3%A0-%EC%96%BB%EA%B8%B0
