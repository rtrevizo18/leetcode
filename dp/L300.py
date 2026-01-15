# 300. Longest Increasing Subsequence
# Medium
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# Status: Complete

# Memoization Solution
class MemoSolution:
    def lengthOfLIS(self, nums) -> int:
        memo = [-1] * len(nums)
        def dp(arr, i):
            if i == 0:
                return 1
            
            if memo[i] != -1:
                return memo[i]
            maximum = 1
            for prev in range(i):
                if arr[prev] < arr[i]:
                    maximum = max(maximum, dp(arr, prev) + 1)
            
            memo[i] = maximum
            return memo[i]
        res = 1
        for idx in range(1, len(nums)):
            res = max(res, dp(nums, idx))
        return res

# Binary Search Solution
class BinarySolution():
    def lengthofLIS(self, arr):
        n = len(arr)
        ans = []

        ans.append(arr[0])

        for i in range(1, n):
            if arr[i] > ans[-1]:
                ans.append(arr[i])
            else:
                low = 0
                high = len(ans) - 1
                while low < high:
                    mid = low + (high - low) // 2
                    if ans[mid] < arr[i]:
                        low = mid + 1
                    else:
                        high = mid
                ans[low] = arr[i]
        return len(ans)