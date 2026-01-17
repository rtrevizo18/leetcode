# 198. House Robber
# Medium
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have
# security systems connected and it will automatically contact the police if
# two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
	def rob(self, nums) -> int:
		n = len(nums) 
		def recursive_rob(i):
			if i >= n:
				return 0
			skip_house = recursive_rob(i+1)
			rob_house = nums[i] + recursive_rob(i+2)	
					
			return max(skip_house, rob_house)
			
		return recursive_rob(0)

class MemoSolution:
	def rob(self, nums) -> int:
		n = len(nums) 
		def recursive_rob(i, memo):
			if i >= n:
				return 0
			if i in memo:
				return memo[i]
			skip_house = recursive_rob(i+1, memo)
			rob_house = nums[i] + recursive_rob(i+2, memo)	
			memo[i] = max(skip_house, rob_house)		
			return memo[i]
		memo = {}	
		return recursive_rob(0, memo)