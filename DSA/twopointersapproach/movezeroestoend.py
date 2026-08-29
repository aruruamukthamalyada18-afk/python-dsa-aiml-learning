nums = [0, 1, 0, 3, 12]
i=0
for j in range(1,len(nums)):
    if nums[j]!=0:
        nums[i]=nums[j]
        i+=1
        nums[j]=nums[i]
print(nums)

    