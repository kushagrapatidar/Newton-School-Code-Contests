def func(nums,len_sub_set): 
    if len(nums)>0:
        sub_set=[]
        for j in range(1,nums[0]+1):
            if j/2 not in sub_set:
                sub_set.append(j)
        len_sub_set.append(len(sub_set))
        len_sub_set=func(nums[1:],len_sub_set)
    return len_sub_set

len_sub_set=[]
nums=[]
for i in range(int(input())):
    nums.append(int(input()))
len_sub_set=func(nums,len_sub_set)
for _ in len_sub_set:
    print(_)