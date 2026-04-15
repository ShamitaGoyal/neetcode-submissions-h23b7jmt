class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        return True 
         


# num -> array of ints
# return true -> value appears more than once
# return false -> value does not appear


