import sys
sys.stdin = open("input.txt","rt")

N = int(input())
seq=[list(map(int,input().split())) for _ in range(N)]

seq.sort(reverse=True)

max_height=[0]*(N)
#head_weight=[0]*(N)
#head_width=[0]*(N)

max_height[0] = seq[0][1]
#head_weight[0] = seq[0][2]
#head_width[0] = seq[0][0]


#print(seq)
for i in range(1,N):
    max_h = 0
#    head_w = 0
#    head_wi= 0
#    print(i)
    for j in range(0,i):
#        print(j,i)
#        print(seq[j],seq[i])
#        print(max_h)
        if seq[i][2] < seq[j][2] and max_h < max_height[j]:
            max_h = max_height[j]
            #head_w = head_weight[j]
            #head_wi = head_width[j]
    
    max_height[i] = max_h + seq[i][1]
    #head_weight[i] = head_w + seq[i][2]
    #head_width[i] = head_wi + seq[i][0]

    
#print(max_height)
print(max(max_height))