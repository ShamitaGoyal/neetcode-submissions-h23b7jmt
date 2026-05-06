class Solution:
    def isValid(self, s: str) -> bool:
        '''
        result = list(s)
        bracketDict = {"(": ")", "[":"]", "{":"}"}
        
        l = 0 
        r = len(result) - 1

        # my solution only works for certain patterns. it doesn't handle everything 
        # if the brackets were close to each other then this solution would fail
        # s = "{} () []"

        while l < r:
            key = result[l]
            if bracketDict[key] == result[r]:
                l += 1 
                r -= 1
            else:
                return False
        return True

        '''
        # ====================================

        '''
        Solution used with stack implementation
        '''

        bracketDict = {"(": ")", "[":"]", "{":"}"}
        stack = []


        for char in s:
            if char in bracketDict:
                stack.append(char)
            else:
                if not stack:
                    return False
                
                last = stack.pop() #the stack only has open brackets like [ ( {
                if bracketDict[last] != char:
                    return False
        return len(stack) == 0
