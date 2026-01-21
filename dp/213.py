# 213. House Robber II
# Medium
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed. All houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one. Meanwhile, adjacent houses
# have a security system connected, and it will automatically contact the police
# if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.


class Solution:
  def rob(self, arr: list[int]) -> int:
    n = len(arr)
    if n == 1:
      return arr[0]
    
    def rob_linear(nums):
      memo = [-1] * len(nums)

      def dfs(i):
          if i < 0:
              return 0
          if memo[i] != -1:
              return memo[i]
          memo[i] = max(
              dfs(i - 1),
              nums[i] + dfs(i - 2)
          )
          return memo[i]

      return dfs(len(nums) - 1)
    
    return max(
            rob_linear(arr[:-1]),  # exclude last
            rob_linear(arr[1:])    # exclude first
        )
