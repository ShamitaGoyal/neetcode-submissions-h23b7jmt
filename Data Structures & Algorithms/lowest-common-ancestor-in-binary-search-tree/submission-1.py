# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        curr = root 

        while curr:
            if p.val > curr.val and q.val > curr.val:
                #go right subtree
                curr = curr.right
            
            elif p.val < curr.val and q.val < curr.val:
                #go left subtree
                curr = curr.left
            
            else:
                #theyve split, or one value is equal to either p or q reutrn it 

                return curr