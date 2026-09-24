# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        #LCA -> the deepest node that has both p and q 
        #somewhere below it (or is one of them itself)

        #key insight -> bst structure tell syou which way to go, no searching needed


        curr = root

        while curr:

            if p.val < curr.val and q.val < curr.val:
                curr = curr.left 
            
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right 
            
            else:
                return curr 