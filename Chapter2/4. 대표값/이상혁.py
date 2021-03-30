import sys
sys.stdin = open("cht2_4_input.txt","rt")

n=int(input())
a = list(map(int,input().split()))
mean_a=round(sum(a) / len(a))

def dev(element):
    return abs(element - mean_a)

dev_list=list(map(dev,a))

test=[a[i] for i,j in enumerate(dev_list) if j == min(dev_list)]
test1 = [i for i,j in enumerate(dev_list) if j == min(dev_list)]

print(mean_a,[test1[i] for i,j in enumerate(test) if j == max(test)][0] + 1)

#out = dict()
#for i, j in enumerate(a):
#    if dev_list[i] ==True:
#        out[i] = a[i]

#def checker1(element):
#    return element == max(out.values())

#check_list1=list(map(checker1,out.values()))
#idx = list(out.keys())[check_list1.index(True)]
#print(mean_a,idx+1)