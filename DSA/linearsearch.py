nums=[4,2,7,1,9]
target=int(input("enter the target"))
found=False
for i in range(len(nums)):
    if nums[i]==target:
        print("target is found at index ",i)
        found=True
        break
if found==False:
    print("not found")