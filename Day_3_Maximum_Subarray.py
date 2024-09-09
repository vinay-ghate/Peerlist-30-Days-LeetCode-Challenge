# Challenge 3 — Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Example: Input: nums = [-2,1,-3,4,-1,2,1,-5,4] Output: 6 Explanation: [4,-1,2,1] has the largest sum = 6.

# https://leetcode.com/problems/maximum-subarray/

import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        x = -sys.maxsize-1
        y = 0
        for i in range(len(nums)):
            y = y+nums[i]
            if y>x:
                x=y
            if y<0:
                y=0
        return x
