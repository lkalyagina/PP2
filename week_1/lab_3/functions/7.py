'''
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
'''
def has_33(nums):
    a = 0
    for i in range(0,len(nums)-2): 
        if nums[i] == 3 and nums[i+1] == 3:
            return True
        else:
            return False



print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
