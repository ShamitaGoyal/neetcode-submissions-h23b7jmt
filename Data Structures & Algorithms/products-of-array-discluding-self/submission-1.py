class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        '''
        my attempt
        result = []
        i = 0 
        j = 0
        length = len(nums)
        while i < length:
            while i != j:
                j += 1
                if i == 0:
                    result.append(maths.prod(nums[j:length]))
                    i += 1 
                if i == length:
                    result.append(maths.prod(nums[0:length]))
                    return 

                result.append(nums[0:i] * nums[j+1: length])
                i += 1
        return result

        '''

        n = len(nums)
        result = [1] * n

        #prefix - everything before the i value 
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]



        #suffix - everything after the i value
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix 
            suffix *= nums[i]

        return result 



