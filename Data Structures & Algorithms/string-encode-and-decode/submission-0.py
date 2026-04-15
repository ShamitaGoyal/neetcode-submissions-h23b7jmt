class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0
        while i < len(s):
            j = i
        
            #step 1: find where number ends
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            
            #step 2: read actual string 
            start = j + 1 
            end = start + length 
            result.append(s[start:end])

            #step 3: move pointer forward 
            i = end 

        return result




        # encode a list of strings to a string
        # strs + strs + strs = str (encoded)
        # ecoded str ---> network 
        # str --> decoded back to strs strs strs strs (orginal list of strings)


