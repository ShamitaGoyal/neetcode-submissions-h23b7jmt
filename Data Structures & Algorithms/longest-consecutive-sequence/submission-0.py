class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #1 remove the dups
        numSet = set(nums)
        longest = 0

        # start for loop
        for num in nums:
            #start counting only if the predecssor does not exist (cuz u dont want to count twice)
            if num - 1 not in numSet:
                #make new var to count the sequence
                length = 1

                #2 keep incrementing the num value to see if that value exists in the set
                # if it exists we keep storing the value of sequence in length 
                # once that num is not in the set, end the loop 
                while num + length in numSet:
                    length += 1 

                #end loop and find the max between longest and length, and store in longest
                longest = max(longest, length)
        # return the longest consecutive sequnec 
        return longest 
