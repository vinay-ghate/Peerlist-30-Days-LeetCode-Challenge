# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


#Method 1
# 1677 ms  17.2 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]


#Method 2
# 53 ms  17.8 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp={}
            n = len(nums)
            for i in range(n):
                temp[nums[i]]=i
            for i in range(n):
                c = target - nums[i]
                if c in temp and temp[c]!=i:
                    return [i,temp[c]]   

# https://leetcode.com/problems/two-sum/
        
