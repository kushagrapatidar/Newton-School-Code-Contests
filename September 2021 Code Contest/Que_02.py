n=int(input())
len_sub_set=[]
for i in range(n):
    num=int(input())
    count=0
    sub_set=[]
    for j in range(num):
        if (j+1)/2 not in sub_set:
            sub_set.append(j+1)
    len_sub_set.append(len(sub_set))
for _ in len_sub_set:
    print(_)