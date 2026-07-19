class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = {}
        if not strs:
            return res
        for s in strs:
            freq = 26 * [0]
            for c in s:
                freq[ord(c)-ord('a')] += 1
            key = tuple(freq)
            if key not in freqMap:
                freqMap[key] = []
            freqMap[key].append(s)
        res = []
        for k, v in freqMap.items():
            res.append(v)
        return res
            

        
        