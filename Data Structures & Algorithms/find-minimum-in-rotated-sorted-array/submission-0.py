class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1

        while l < r:

            mid = (l + r) // 2

            # if the mid value is higher than the right value
            # the min value must be on the right side
            if nums[mid] > nums[r]:
                l = mid + 1 
                # move the left pointer to one place higher than mid pointer
            
            else:
                r = mid
                # if the mid value is lower than right, make the r = mid 
                # and keep the loop going until the left pointer has hit the min value
        return nums[l] #this means l == r we found the min
        