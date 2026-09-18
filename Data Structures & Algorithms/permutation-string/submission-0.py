class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        count1 = {}

        for c in s1:
            count1[c] = 1 + count1.get(c,0)
        
        left = 0
        count2 = {}

        for right in range(len(s2)):
            count2[s2[right]] = 1 + count2.get(s2[right], 0)

            #keep window size len(s1) because it is fixed

            if (right - left + 1) > len(s1):
                count2[s2[left]] -= 1

                if count2[s2[left]] == 0:
                    del count2[s2[left]] 
                
                left += 1 
            if count1 == count2:
                return True 
        return False



