nums=[2,1,5,1,3,2]
k=3
i=0
j=0
max_sum=0
sum=0
while j<k:
    sum+=nums[j]
    max_sum=sum
    j+=1
while j<len(nums):
    sum=sum+nums[j]
    sum=sum-nums[i]
    max_sum=max(max_sum,sum)
    i+=1
    j+=1
print(max_sum)