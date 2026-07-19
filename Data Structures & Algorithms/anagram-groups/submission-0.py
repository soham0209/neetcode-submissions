class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}
        for s in strs:
            freq_count = 26*[0]
            for c in s:
                k = ord(c) - ord('a')
                freq_count[k] += 1
            key = tuple([str(k) for k in freq_count])
            
            if key not in hash_table:
                hash_table[key] = [s]
            else:
                hash_table[key].append(s)
        res = [v for k, v in hash_table.items()]
        return res
            
        