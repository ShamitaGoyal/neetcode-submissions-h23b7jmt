class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "":
            return ""

        
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)

        #have ->tracks distinct chars + their count
        #need -> how many chars we need (distinct chars)

        res, resLen = [-1,-1], float("infinity")
        left = 0 

        for right in range(len(s)):
            window[s[right]] = 1 + window.get(s[right], 0)

            #we need to check if our have condition is getting satisfied 

            if s[right] in countT and countT[s[right]] == window[s[right]]:
                have += 1 
            
            while have == need:
                # when to shrink the window

                if (right - left + 1) < resLen:
                    res  = [left, right]
                    resLen = right - left + 1

                window[s[left]] -=1

                if s[left] in countT and  window[s[left]] < countT[s[left]]:
                    have -=1 
                
                left += 1 

        left, right = res 
        return  s[left: right + 1] if resLen != float("infinity") else ""




