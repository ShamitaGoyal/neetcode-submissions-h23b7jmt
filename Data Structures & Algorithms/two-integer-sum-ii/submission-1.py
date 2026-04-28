class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0 
        r = len(numbers) - 1

        # target - l + r (if target is too big then we move r to left)
        # if target is too small then we move l to right 

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum < target:
                l += 1 
            elif sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]
            

            
