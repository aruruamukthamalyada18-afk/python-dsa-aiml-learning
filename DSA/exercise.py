"""name="john smith"
age=20
status="new patient"
print(name,"\n",age,"\n",status)"""
#taking input from user
"""name=input("what is your name? ")
print("hello",name)"""
#typeconversion
"""birth_year=input("enter your birth_year:")
age=2026-int(birth_year)
print(age)"""
#calculate
"""first=float(input("enter the  first value:"))
second=int(input("enter the second value:"))
sum=first+second
print("sum:",sum)"""     
#if statement
"""temparature=int(input("enter the temperature:"))
if temparature>30:
     print("it is a hot day")
print("done")"""
#exercise
"""for i in range(1,10):
    if i%2==0:
        print(i)
print("we have 4 even numbers")"""
#basic problems
#print 1 to 10 numbers
"""for i in range(1,11):
    print(i)"""
#print squares of 1 to 10 
"""for i in range(1,11):
    print(i*i)"""
#print even numbers 1 to 20 
"""for i in range(1,21):
    if i%2==0:
        print(i)"""
#print odd numbers 1 to 20 
"""for i in range(1,21):
    if i%2!=0:
        print(i)"""
#print reverse 10 down to 1 
"""for i in range(10,0,-1):
    print(i)"""
#print multiples 10 multiples of 5 
"""for in range(1,11):
    print(5*i)"""
#print sum of 1 to 10 numbers 
"""sum=0
for i in range(1,11):
    sum=sum+i
    print(sum)"""
#greaterthan
"""a=int(input("enter frist number"))
b=int(input("enter second number"))
if a>b:
    print("a is gratest number")
elif b<a:
    print("b is greatest number")
else:
    print("both are same")"""
#Print numbers between 1 and 100 that are divisible by 5 
"""for i in range(1,101):
    if i%5==0:
        print(i)"""
 #Print numbers between 1 and 100 that are divisible by both 3 and 5.       
"""for i in range(1,101):
    if i%5==0 and i%3==0:
        print(i)"""
#Count how many numbers are positive and how many are negative.
numbers = [10, -5, 8, -3, 0, 7, -2]

"""positive_count = 0
negative_count = 0

for i in numbers:
    if i > 0:
        positive_count += 1
    elif i < 0:
        negative_count += 1

print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)"""
#find largest number without using num
"""numbers=[10,5,8,3,12,7]
largest=numbers[0]
for i in numbers:
    if i >largest:
        largest=i
print(largest)"""
#find smallest number with out using min
"""numbers = [10, 5, 8, 3, 12, 7]
smallest=numbers[0]
for i in numbers:
    if i<smallest:
        smallest=i
print(smallest)"""
#count how many nubers are there
"""numbers = [2, 5, 2, 8, 2, 10, 5]
target=int(input("enter the number"))
count=0
for i in numbers:
    if i==target:
        count=count+1
print(count,"times")"""
#find sum of numbers without using sum
"""numbers = [10, 5, 8, 3, 12, 7]
a=0
for i in numbers:
    a=a+i
print(a)"""
#count how many even and odd numbers
"""numbers = [10, 5, 8, 3, 12, 7]
count=0
total=0
for i in numbers:
    if i%2==0:
        count=count+1
        total=i
        print("even numbers",total)
    elif i%2!=0:
        count=count+1
        total=i
        print("odd numbers",total)"""
#swapping
"""a=int(input("enter the a value:"))
b=int(input("enter the b value:"))
a,b=b,a
print("after swapping:","a=",a, "b=",b)"""
#sum
"""a=int(input("enter the a value:"))
b=int(input("enter the b value:"))
sum=0
sum=a+b
print("sum of two values a and b=",sum)"""
#factorial
"""n=int(input("enter the value"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial of value",fact)"""
#product of  first n munbers
"""n=int(input("enter the number"))
product=1
for i in range(1,n+1):
    product=product*i
print("product:",product)"""
#fibonacci
"""n=int(input("enter the number"))
a=0
b=1
for i in range(n):
    print(a,end="")
    fib=a+b
    a=b
    b=fib"""
#check prime number
"""n= int(input("enter the number"))
for i in range(n):
    if i%2==0:
        print("prime")
    else:
        print("not prime")"""
"""n=int(input("enter the value"))
count=0
while n>0:
    n=n//10
    count=count+1
print(count)"""
"""n=int(input("enter the value"))
sum=0
while(n>0):
    digit=n%10
    sum=sum+digit
    n=n//10
print(sum)"""
"""n=int(input("enter the value"))
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print(reverse)"""
#break statement
"""n=int(input("enter the value"))
for i in range(2,n//2-1):
    if n%i==0:
        break
print(i)"""
        
    
    
        

    
    
    
        