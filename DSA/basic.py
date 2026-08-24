#ifelseif
"""class solution:
    def studentgrade(self,marks):
        if marks>=90:
            return"GRADE A"
        elif marks>=70:
            return"GRADE B"
        elif marks>=50:
            return"GRADE C"
        elif marks>=35:
            return"GRADE D"
        else:
            return "FALSE"
obj=solution()
answer=obj.studentgrade(int(input("enter the student marks:")))
print(answer)"""
#forloop
#add low and high numbers
"""low=int(input("enter the low value"))
high=int(input("enter the high value"))
sum=0
for i in range(low,high+1):
    sum=sum+i
print("sum of low and high",sum)"""
#Given a digit d (0 to 9), find the sum of the first 50 positive integers (integers > 0) that end with digit d.
"""class solution:
    def whileloop(self,d:int):
        sum=0
        for i in range(50):
            sum=sum+(i*10+d)
        return sum
obj=solution()
print(obj.whileloop(1))"""
#Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.
"""n = int(input("enter the values of array"))

array = list(map(int, input().split()))

left = 0
right = n - 1

while left < right:
    array[left], array[right] = array[right], array[left]
    left += 1
    right -= 1

print(array)"""
    
    
    

        
    
    

    


   
    
    