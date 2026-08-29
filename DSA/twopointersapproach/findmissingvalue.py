"""nums=[3,0,1]
for i in range(0,len(nums)+1):
    if i not in nums:
        print(i)"""
"""nums = [9,6,4,2,3,5,7,0,1]
for i in range(0,len(nums)+1):
    if i not in nums:
        print(i)"""
"""time complexity for this o(n^2) and space complexity o(n)"""




nums = [9,6,4,2,3,5,7,0,1]
n=len(nums)
expected=n*(n+1)//2
actual=0
for i in nums:
    actual+=i
missing=expected-actual
print(missing)
    
"""timecomplexity:o(n)
space complecity:o(1)"""


