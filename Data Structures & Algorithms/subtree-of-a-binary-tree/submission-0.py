# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        #uses same logic as isSameTree because we will need to validate if at the root if both variables have the same nodes at that node 

        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True 
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    
    def isSameTree(self, p,q):
        if not p and not q:
            return True 
        
        if not p or not q or p.val != q.val:
            return False 
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



        # complexity O(mxn) worst case, where m = nodes in A, n= nodes in B
        #for every node in A  you mgith do a full O(n) comparison
        #first example of reusing a simpler tree pattern as a building block, the same way reorder list reused reverse linked list 