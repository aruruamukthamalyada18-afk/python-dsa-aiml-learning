heights = [1,8,6,2,5,4,8,3,7]
max_area=0
left=0
right=len(heights)-1
while left<right:
    height=min(heights[left],heights[right])
    width=right-left
    area=height*width
    if area>max_area:
        max_area=area
    if heights[left]<heights[right]:
        left+=1
    else:
        right-=1
print(max_area)

"""time complexity:o(n)
space complexity:o(1)"""
    
    
    