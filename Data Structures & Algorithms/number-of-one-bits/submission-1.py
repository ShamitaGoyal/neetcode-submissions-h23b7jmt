class Solution:
    def hammingWeight(self, n: int) -> int:
        #n = 23
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res

    #tc -> O(1)

'''
Start       
10111    → res = 0
    ↓
10110    → res = 1
    ↓
10100    → res = 2
    ↓
10000    → res = 3
    ↓
00000    → res = 4
            '''