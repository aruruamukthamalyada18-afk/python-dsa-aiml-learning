nums = [-1, 0, 1, 2, -1, -4]
target=int(input("enter the target"))
nums.sort()
for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i-1]:
       continue
    left=i+1
    right=len(nums)-1
    while left<right:
        total=nums[left]+nums[i]+nums[right]
        if total==target:
            print(nums[left],"+",nums[i],"+",nums[right],"=",target)
            left+=1
            right-=1
        elif total<target:
            left+=1
        else:
            right-=1
"""time complexity :o(n)
space complexity:O(1)"""