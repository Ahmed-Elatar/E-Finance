def removeDuplicates( nums):
    
    n = len(nums)
    for i in range(n-1,0,-1):
        if nums[i] == nums[i-1]:
            nums.pop(i)
     
    return len(nums)    
    


nums = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(nums))