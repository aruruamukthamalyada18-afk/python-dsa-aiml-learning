nums=[1,2,3,4,5]
k=int(input("enter the value of k"))
k=k%len(nums)
print(nums[k:]+nums[:k])

        