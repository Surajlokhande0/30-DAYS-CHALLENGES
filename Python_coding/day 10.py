def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        
        if slow == fast:
            break
    
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

array = [1, 3, 4, 2, 2]
duplicate = findDuplicate(array)
print("The duplicate element is:", duplicate)
