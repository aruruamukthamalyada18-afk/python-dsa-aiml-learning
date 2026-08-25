"""nums=[3,3,6,1]
max=nums[0]
for i in nums:
    if i>max:
        max=i
print(max)"""
"""largestelement"""
"""class solution:
    def largest_element(self,nums):
        max=nums[0]
        for i in nums:
            if i>max:
                max=i
        return max
obj=solution()
print(obj.largest_element([3,3,6,1]))"""
"""class solution:
    def largest_element(self,nums):
        max=nums[0]
        for i in nums:
            if i>max:
                max=i
        return max
nums = list(map(int,input("enter the array elements").split()))

obj=solution()
print(obj.largest_element(nums))"""
"""nums=list(map(int,input("enter the array elements").split()))
if len(nums)<2:
    print(-1)
else:
    largest=nums[0]
    second_largest=nums[1]
    for i in nums:
        if i>largest:
            second_largest=largest
            largest=i
        elif i>second_largest and i!=largest:
            second_largest=i
    if second_largest==largest:
        print(-1)
    else:
        print(second_largest)"""
"""nums=list(map(int,input("enter the values").split()))
for i in range (len(nums)-1):
    if nums[i]>nums[i+1]:
        print("False")
    break 
else:
        print("True")"""
"""nums=list(map(int,input("enter the values").split())) 
nums.sort()    
i=0
for j in range(1,len(nums)):
    if nums[i]!=nums[j]:
        i=i+1
        nums[i]=nums[j]
print(nums[: i+1])"""
"""nums=list(map(int,input("enter the array elements").split()))
nums[0],nums[-1]=nums[-1],nums[0]
print(nums)"""
"""nums=list(map(int,input("enter the array elements").split()))
k=int(input("enter k"))
print(nums[k:]+nums[:k])"""
"""nums=list(map(int,input("enter the elements").split()))
for i in nums:
    if i in nums:
        if i==0:
            i=nums[-1]
    print(i)"""
"""nums=list(map(int,input("enter the array elements").split()))
target=int(input("enter the target"))
i=0
j=len(nums)-1
while i<j:
    sum=nums[i]+nums[j]
    if sum==target:
        print(nums[i],"+",nums[j],"=",sum)
        break
    elif sum>target:
        j-=1
    else:
        i+=1"""
"""nums=list(map(int,input("enter the array elements").split()))
i=0
j=len(nums)-1
while i<j:
    nums[i],nums[j]=nums[j],nums[i]
    i+=1
    j-=1
print(nums)"""
"""s=str(input("enter the string"))
right=len(s)-1
left=0
while left<right:
    if s[left]!=s[right]:
        print("False") 
        break
    left+=1
    right-=1
else:
    print("True")"""
"""nums=list(map(int,input("enter the array elements").split()))
target=int(input("enter the target"))
left=0
right=len(nums)-1
nums.sort()
while left<right:
    sum=nums[left]+nums[right]
    if sum==target:
        print(nums[left],"+",nums[right],"=",sum)
        break
    elif sum<target:
        left+=1
    else:
        right-=1"""
"""heights=list(map(int,input("enter the array elements").split()))
left=0
right=len(heights)-1
max_area=0
while left<right:
    height=min(heights[left],heights[right])
    width=right-left
    area=height*width
    if area > max_area:
        max_area = area
    if heights[left]<heights[right]:
        left+=1
    else:
        right-=1
print(max_area)"""
"""nums=list(map(int,input("enter the array elements").split()))
nums.sort()
i=0
for j in range (1,len(nums)):
    if nums[i]!=nums[j]:
        i+=1
        nums[i]=nums[j]
print(nums[: i+1])"""
"""nums=[0,1,0,3,12]
slow=0
for fast in range(len(nums)):
    if nums[fast]!=0:
        nums[fast],nums[slow]=nums[slow],nums[fast]
        slow+=1
print(nums)"""
"""nums1=[1,2,3,4,5]
nums2=[1,2,6,7]
union=[]
for i in nums1:
    if i not in union:
        union.append(i)
for i in nums2:
    if i not in union:
        union.append(i)
print(union)"""
"""nums=[5,2,8,1,3]
largest_element=nums[0]
for i in nums:
    if i>largest_element:
        largest_element=i
print(largest_element)"""
"""time complexity:0(n)
space complexity:0(1)"""
"""nums=[5,2,8,1,3]
largest_element=nums[0]
second_largest=nums[0]
for i in nums:
    if i>largest_element:
        second_largest=largest_element
        largest_element=i
    elif i>second_largest and i!=largest_element:
        second_largest=i
print(second_largest)"""
"""nums=[1,2,5,3,4,5]
is_sorted=True
for i in range(1,len(nums)):
    if nums[i-1]>nums[i]:
        is_sorted=False
        break
if is_sorted:
    print("sorted")
else:
    print("not sorted")"""
"""nums=[1,2,8,4,9,5]
left=0
right=len(nums)-1
while left<right:
    nums[left],nums[right]=nums[right],nums[left]
    left+=1
    right-=1
print(nums)"""  
"""nums=[1,1,2,2,8,8,3,3,4,4]
i=0
for j in range(1,len(nums)):
    if nums[i]!=nums[j]:
        i=i+1
        nums[i]=nums[j]
print(nums[:i+1])"""
"""s="python"
reverse=""
for i in range(len(s)-1,-1,-1):
    reverse+=s[i]
print(reverse)"""
"""s=str(input("enter the string"))
right=len(s)-1
left=0
while left<right:
    if s[left]!=s[right]:
        print("not palindrome")
        break
    left+=1
    right-=1
else:
    print("palindrome")"""
"""nums=[1,3,8,5,4]
maximum=nums[0]
for i in range(1,len(nums)):
    if nums[i]>maximum:
        maximum=nums[i]
print(maximum)"""
"""nums=[1,1,2,3,2,4]
frequency={}
for num in nums:
    if num in frequency:
        frequency[num]+=1
    else:
        frequency[num]=1
print(frequency)"""
"""nums=[1,2,1,2,3,4,5,4]
i=0
nums.sort()
for j in range (1,len(nums)):
    if nums[i]!=nums[j]:
        i=i+1
        nums[i]=nums[j]
print(nums[:i+1])"""
"""nums=[2,7,11,15]
target=9
left=0
right=len(nums)-1
while left<right:
    total=nums[left]+nums[right]
    if total==target:
        print(nums[left],"+",nums[right],"=",target)
        break
    elif total<target:
        left+=1
    else:
        right-=1"""
"""nums=[1,2,3,4]
for i in range(1,6):
    if i not in nums:
        print(i)"""
"""s="programming"
count=0
for i in s:
    if i in "aeiou":
        count+=1
print(count)"""
"""nums=[8,3,5,1,4]
largest=nums[0]
second=float("-inf")
for i in range(1,len(nums)):
    if nums[i]>largest:
        second=largest
        largest=nums[i]
    elif nums[i]>second and nums[i]!=largest:
        second=nums[i]
print(second)"""
"""nums=[1,2,3,4,5]
sorted_array=True
for i in range(1,len(nums)):
    if nums[i]<nums[i-1]:
        sorted_array=False
        break
if sorted_array:
    print("sorted")
else:
    print("not sorted")"""
nums = [1, 2, 3, 4, 5]

first = nums[0]

for i in range(1, len(nums)):
    nums[i-1] = nums[i]

nums[len(nums)-1] = first

print(nums)
    
    
        


        
    

    

    
        
        

        

        

