# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        '''
        similar to the min window substring, sliding window problem -> we needed pos infinity 
        for that because we needed a starting placehoder that's bigger than any real answer (positive)
        guaranteed to lose tot eh first real legnth you compute

        - here we are hunting for the largest path sum, so you need the oppsite -> a starting placeholder that's smaller than any real answer -> (negative), guaranteed to lose (in the max comparison) to the first real sum you compute. if you did positive inf, it will always wind the max

        - why not 0 -> becuz 0 might not actually be a possible answer here -> if every node in the tree is negative, the real answer has to be negative too (you must pick a path , you cant pick nothing). if you start at 0,0 wins by default and gives you the wrong answer that has never even achieavle. -infinity guaranteed the very first real number you compute always beats it, no matter how negative that number is
        '''
        max_sum = float('-inf')

        def dfs(node):
            #nonlocal used so u can update var becuz it is nonlocal scoped
            nonlocal max_sum
            if not node:
                return 0
            

            leftGain = max(dfs(node.left), 0)
            rightGain = max(dfs(node.right),0)

            bend_val = node.val + leftGain + rightGain
            max_sum = max(max_sum,bend_val)

            return node.val + max(leftGain, rightGain)
        
        dfs(root)
        return max_sum