# 62. Unique Paths
# Medium
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take
# to reach the bottom-right corner.


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def uniquePaths_helper(i, j, memo):
            if i == m or j == n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) not in memo:
                memo[(i, j)] = uniquePaths_helper(i, j + 1, memo) + uniquePaths_helper(i + 1, j, memo)

            return memo[(i, j)]
        memo = {}
        return uniquePaths_helper(0, 0, memo)