from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        self.s = s
        self.t = t
        str1 = collections.Counter(self.s)
        str2 = collections.Counter(self.t)
        if str1 == str2:
            return True
        else:
            return False
        
        # print(str1)


# s = "racecar"
# t = "carrace"
# case1 = Solution()
# case1.isAnagram(s,t)



# string 1 --> s 
# string 2 --> t 
# return True --> string 1 & string 2 are anagrams of each other
# return False --> string 1 & 2 are NOT anagrams of each other 

# anagram --> a string that contains the exact same chars as another string