# 63. Unique Paths II
# Medium
# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid.
# A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid)-> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        def helper(i, j, memo):
            if m == i or n == j:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) not in memo:
                memo[(i, j)] = helper(i, j + 1, memo) + helper(i + 1, j, memo)
            return memo[(i, j)]
        memo = {}
        return helper(0, 0, memo) 