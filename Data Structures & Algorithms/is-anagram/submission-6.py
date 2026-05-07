class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #same number of chars in both strs but can be any order

        sDict = defaultdict(int)
        tDict = defaultdict(int)

        for char in s: #runs n times
            if char not in sDict:
                sDict[char] += 1
            else:
                sDict[char] += 1


        #this creates a dict of counts for the s string
        # which we can compare with the t string now 
        
        for char in t: #runs n times
            if char not in tDict:
                tDict[char] += 1
            else:
                tDict[char] += 1
        
        return sDict == tDict 


#tc -> O(n)


# if char is in dict -> add one 
# otherwise if not -> 