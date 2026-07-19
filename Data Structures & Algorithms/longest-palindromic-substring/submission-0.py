class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        max_len = 0
        def check_pali(i, j):
            pal_len = j - i + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i-=1
                j+=1
                pal_len = j - i + 1
            return pal_len, i+1, j
        for i in range(len(s)):
            odd_count, l_odd, r_odd = check_pali(i, i)
            even_count, l_even, r_even = check_pali(i, i+1)
            if odd_count > max_len:
                max_len = odd_count
                ans = s[l_odd:r_odd]
            if even_count > max_len:
                max_len = even_count
                ans = s[l_even:r_even]
        return ans
            
                


            
        