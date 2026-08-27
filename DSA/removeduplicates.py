nums = [1,1,2,2,3,3,4,4]
i=0
for j in range(1,len(nums)):
    if nums[i]!=nums[j]:
        i+=1
    nums[i]=nums[j]
print(nums[: i+1])
"""time complexity:o(n)
space complexity:o(1)"""