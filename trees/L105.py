# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Medium
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree
# and inorder is the inorder traversal of the same tree, construct and return the binary tree.
# Status: Complete


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTreeRecursively(self, mp, preorder, preindex, left, right):
      if left > right:
          return None

      rootVal = preorder[preindex[0]]
      preindex[0] += 1
      root = TreeNode(rootVal)
      index = mp[rootVal]

      root.left = self.buildTreeRecursively(mp, preorder, preindex, left, index - 1)
      root.right = self.buildTreeRecursively(mp, preorder, preindex, index + 1, right)

      return root

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
      mp = {value: idx for idx, value in enumerate(inorder)}
      preindex = [0]
      
      return self.buildTreeRecursively(mp, preorder, preindex, 0, len(inorder) - 1)