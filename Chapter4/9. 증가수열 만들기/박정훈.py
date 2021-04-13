import sys

#sys.stdin=open('input.txt','rt')

n = map(int,input().split())

numbers = list(map(int,input().split()))

answer = list()
character = ''


while numbers :
    if len(numbers) == 1:
        if numbers[0] > answer[-1]:
            answer.append(numbers[0])
        break
    if numbers[0] > numbers[-1]:
        answer.append(numbers[-1])
        character = character + 'R'
        numbers.pop(0)

    elif numbers[0] < numbers[-1]:
        answer.append(numbers[0])
        character = character + 'L'
        numbers.pop()

print(len(answer))
print(character)
