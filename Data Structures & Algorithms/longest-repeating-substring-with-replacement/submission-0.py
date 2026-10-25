class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r  = 0, 0
        freq = {}

        res = 0
        while r < len(s):
            if s[r] not in freq:
                freq[s[r]] = 0
            freq[s[r]] += 1
           
            if r-l+1 - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1 
            else:
                res = max(res, r-l+1)
            
            r += 1

        return res