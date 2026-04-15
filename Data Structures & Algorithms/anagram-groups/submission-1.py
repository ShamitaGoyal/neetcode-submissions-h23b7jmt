class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                # you cant have a list as a key value in dict 
                # you need to turn the key into a string or tupple
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
            