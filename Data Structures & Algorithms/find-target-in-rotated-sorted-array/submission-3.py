class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0 
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            #checks if mid value is already target then return it
            if nums[mid] == target:
                return mid 
            

            # check for which part is sorted

            #1) checks for the left side is sorted 

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # 2) checks for the right side is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1 


            

