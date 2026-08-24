"""n = int(input("enter the size :"))
for i in range(n):
    for j in range(n):
        print("*",end="")
        
    print()"""
#second pattern
"""n = int(input("enter no of rows:"))
for i in range(1,n+1):
    for j in range(i):
        print("*" , end="")
    print()"""  
    
"""n=int(input("enter the no of rows"))
for i in range(1,n):
    for j in range(i):
        print("*",end="")
    print()"""


#pattern3
"""n = int(input("Enter no of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()"""

#pattern4
"""n=int(input("enter no of rows")) 
for i in range(1,n+1):
    for j in range(0,n-i+1):
        print("*",end="")
    print()"""

#pattern6
"""n=int(input("enter no of rows"))
for i in range(0,n+1):
    for j in range(1,n-i+1):
        print(j,end="")
    print()"""
    
#pattern7
"""n=int(input("enter no of rows:"))
for i in range(0,n):
    #space
    for j in range(0,n-i-1):
        print(" ",end="")
        #star
    for j in range(0,2*i+1):
        print("*",end="")
            #space
    for j in range(0,n-i-1):
        print(" ",end="")
    print()"""

#pattern8
"""n=int(input("enter no of rows:"))
for i in range(0,n):
    #space
    for j in range(0,i):
        print(" ",end="")
        #star
    for j in range(0,2*n-(2*i+1)):
        print("*",end="")
        #space
    for j in range(0,i):
        print(" ",end="")
    print()"""
 #pattern9   
n=int(input("enter no of rows:"))
for i in range(0,n):
    #space
    for j in range(0,n-i-1):
        print(" ",end="")
        #star
    for j in range(0,2*i+1):
        print("*",end="")
            #space
    for j in range(0,n-i-1):
        print(" ",end="")
    print()
for i in range(0,n):
    #space
    for j in range(0,i):
        print(" ",end="")
        #star
    for j in range(0,2*n-(2*i+1)):
        print("*",end="")
        #space
    for j in range(0,i):
        print(" ",end="")
    print()