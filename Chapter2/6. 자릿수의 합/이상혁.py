import sys
sys.stdin = open("cht2_6_input.txt","rt")

n=int(input())
a = list(map(int,input().split()))

#print(n,a)
each_list=list(map(int,list('1234')))
#print(sum(each_list))

def digin_sum(element):
    each_list=list(map(int,list(str(element))))
    return sum(each_list)


list_of_sum=list(map(digin_sum,a))
max_list=[a[idx] for idx, v in enumerate(list_of_sum) if v == max(list_of_sum)]

print(max_list[0])