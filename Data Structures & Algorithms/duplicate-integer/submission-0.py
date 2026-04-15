class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.nums = nums 
        self.nums2 = set(self.nums)
        if len(self.nums) == len(self.nums2):
            return False
        else:
            return True 



         




# nums --> list of integers
# return true --> integer appears more than once in list (more than once)
# return false --> integer doesn't appear more than once in list (only once)