class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0 
        best = 0
        window = set()

        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left +=1 
            
            window.add(s[right])
            best = max(best, len(window))
        return best