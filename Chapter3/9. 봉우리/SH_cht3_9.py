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

coparison_out1=list(map(comparison,matrix))
coparison_out2=list(map(comparison,inv))

summ=[coparison_out1[i][j] +coparison_out2[i][j] for i in range(indicator) for j in range(indicator) ]

print(summ)

print(summ.count(2))