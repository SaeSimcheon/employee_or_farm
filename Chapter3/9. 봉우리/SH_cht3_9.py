import sys
sys.stdin = open("cht3_9_input.txt","rt")

indicator = int(input())
matrix = list()

for i in range(indicator):
    matrix.append(list(map(int,input().split())))


def comparison(element):
    output = list()
    element.insert(0,0)
    element.append(0)
    print(element)
    for i in range(1,indicator+1):
        if (element[i-1] < element[i]) & (element[i+1] < element[i]):
            output.append(True)
        else:
            output.append(False)
    return output
        
inv = list(map(list,zip(*matrix)))

comparison_out1=list(map(comparison,matrix))

comparison_out2=list(map(comparison,inv))
inv_com = list(map(list,zip(*comparison_out2)))


summ=[comparison_out1[i][j] +inv_com[i][j] for i in range(indicator) for j in range(indicator) ]

print(summ)

print(summ.count(2))