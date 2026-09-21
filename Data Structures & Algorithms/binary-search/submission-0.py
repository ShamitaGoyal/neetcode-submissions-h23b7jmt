class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1


        while low <= high:
            mid = low + (high  - low) //2


            #check if x is present at mid 
            if nums[mid] == target:
                return mid 
            
            #if target is greater, ignore left half

            elif nums[mid] < target:
                low = mid + 1 
            
            #if x is smaller, ignore right half 
            else:
                high = mid - 1
            
        #if x is smaller, ignore right half
        return -1