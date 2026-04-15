class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {}

        #nums = [3,4,5,6], target = 7
        #Output: [0,1]

        # Input: nums = [4,5,6], target = 10
        # Output: [0,2]

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        


# {3:0, 4:1, 5:2, 6:3 }

# i=0, n=4
# diff = 6
# {4:0}

# i=1, n=5
# diff = 5
# {4:0, 5:1}

# i=2, n=6
# diff = 4
#[prevMap[4], 2]
#[0,2]