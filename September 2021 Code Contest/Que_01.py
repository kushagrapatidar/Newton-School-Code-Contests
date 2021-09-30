nums=input()
nums=nums.split()
for i in range(len(nums)):
    nums[i]=int(nums[i])
lst=[0,1,2]
lst[2]=max(max(nums[0],nums[1]),nums[2])
lst[0]=min(min(nums[0],nums[1]),nums[2])
for _ in nums:
    if _ not in lst:
        lst[1]=_
print(lst[1])


