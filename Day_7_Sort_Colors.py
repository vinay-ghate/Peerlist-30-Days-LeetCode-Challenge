# Challenge 7 — Sort Colors
# Problem: Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# Example: Input: nums = [2,0,2,1,1,0] Output: [0,0,1,1,2,2]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        while True:
            if i==len(nums)-1:
                return nums
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
                i = 0
                continue
            i+=1
        

# https://leetcode.com/problems/sort-colors/submissions/
