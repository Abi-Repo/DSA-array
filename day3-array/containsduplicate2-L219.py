# Given an integer array nums and an integer k,
# return true if there are two distinct indices i and j 
# in the array such that nums[i] == nums[j] and abs(i - j) <= k.
# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

def containsfuplicate2(nums, k):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]==nums[j] and abs(i-j)<=k:
                return True
    return False
        
nums = [1,2,3,1]
k=3
res = containsfuplicate2(nums,k)
print(res)

