# 53. Maximum Subarray
# Medium
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums) -> int:
        res = nums[0]

        maxEnding = nums[0]

        for i in range(1, len(nums)):
            
            maxEnding = max(maxEnding + nums[i], nums[i])

            res = max(res, maxEnding)
        
        return res