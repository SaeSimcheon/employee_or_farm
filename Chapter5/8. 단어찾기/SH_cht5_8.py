import sys
sys.stdin=open("input.txt", "r")
n=int(input())
candidates= [input() for _ in range(n)]
used= [input() for _ in range(n-1)]

print(candidates , used)

for word in candidates:
    if word not in used:
        print(word)
        break
    else:
        continue