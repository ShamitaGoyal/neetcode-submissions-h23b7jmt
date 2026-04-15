class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # nums -> array of ints
        # k-> int which is how many frequent elements within the array
        #return as an array which elements occur the most k 

        #idea1 using a set?

        #loop through and do a unique count and return the dict with the 
        #vals with the most count

        '''

        dictCount = defaultdict(int)
        for n in nums:
            dictCount[n] += 1

        sortedDictCount = sorted(dictCount.items(), key=lambda x: x[1], reverse=True)
        return [key for key, val in sortedDictCount[:k]]
        '''
        
        # [1:1, 2:2, 3:3]
        # how to find the largest value for which key
        # my solution was to count the frequency of each 
        #number and then sort the array and then 
        #tc: O(n log n)


        # STEP 1: make a frequency map
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        
        # STEP 2: make the buckets, map each freq in the buckets
        n = len(nums)
        buckets = [[] for _ in range(n+1)]
        for num, count in freq.items():
            buckets[count].append(num)


        #  STEP 3: find the top k frequent elements
        result = []
        for i in range(n, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
                



