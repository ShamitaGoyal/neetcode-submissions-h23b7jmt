class Solution:
    def isPalindrome(self, s: str) -> bool:
         #O(n) --> because left moves only n times inwards and right 
         # moves only n times inwards (no more than that) thats why 
         #the time of this alg is linear 
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while right > left and not self.alphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left = left + 1
            right = right - 1
        return True

        
    def alphaNum(self,c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))