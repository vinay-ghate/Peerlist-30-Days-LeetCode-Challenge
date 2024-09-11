# Challenge 4 — Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. The product of any prefix or suffix of nums of length 1 is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.

# Example: Input: nums = [1,2,3,4] Output: [24,12,8,6]

# 491 ms 31 MB
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = 1
        cnt = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                a = a*nums[i]
            else:
                if cnt==1:
                    return [0 for i in nums]
                cnt+=1
                pass
        b = nums
        for i in range(len(nums)):
            if nums[i]!=0:
                b[i]= a//nums[i]
            else:
                nums = [0 for i in nums]
                nums[i] = a
                return nums
        return nums

# https://leetcode.com/problems/maximum-subarray
