#traversal
"""arr=[10,20,30,40] #list created
for i in arr:
    print(i)"""


#list methods
"""arr =[10,20,30,40]
print("original list", arr)""" #if we use array name in print then it print like array

#append()
"""arr.append(50)
arr.append(100)
print("after append:",arr)"""

#insert()
"""arr.insert(2,25)
arr.insert(4,35)
arr.insert(4,38)
arr.insert(4,45)
print("after insert:",arr)"""

#remove()
"""arr.remove(20)
print("after remove:",arr)"""

#pop()
"""arr.pop(3)
print("after pop:",arr)"""

#index()#finding position
"""print("index of 30:",arr.index(30))
print("index of 40: ",arr.index(40))"""

#count()
"""arr.append(30)
arr.append(20)
print("count of 30:",arr.count(30))
print("count of 20:",arr.count(20))
print("count of 10:",arr.count(10))"""

#sort()
"""arr.sort()
print("after sort:",arr)"""

#day1
"""arr=[10,5,8,3,12,7]
print("elements in array:",arr)"""
#to print all elements one by one use loops
"""arr=[10,5,8,3,12,7]
for i in range(len(arr)):
    print(arr[i])"""
#sum of all elements
"""arr=[10,5,8,3,12,7]
sum=0
for i in range(len(arr)):
    sum=arr[i]
    print("sum of all elements:",arr[i])"""
#day1 find largest element in array
"""def find_largest(arr):#bruteforce approach
    max_element=arr[0]
    for num in arr:
        if num>max_element:
            max_element=num
    return max_element
arr=[10,20,4,45,99]
print("largesteleement:",find_largest(arr))"""
#optimal solution
"""arr=[10,20,4,45,99]
print("largestelement:",max(arr))"""
#problem2 find second largest element in the array
#bruteforce solution
"""def brute_force(arr):
    sorted_arr=sorted(arr,reverse=True)
    return sorted_arr[1]

arr=[3,5,1,2,4,8,7]
print("secondlargest:",brute_force(arr))"""
#optimal solution
"""def optimal_sol(arr):
    largest=secondlargest=float("-inf")
    for num in arr:
        if num>largest:
            secondlargest=largest
            largest=num
        elif num>secondlargest and num!=largest:
            secondlargest=num
    if secondlargest!=float("-inf"):
        
         return secondlargest
     
         return "not found"
    
        
arr=[3,5,1,2,4,8,7]
print("secondlargest:",optimal_sol(arr))"""



    
