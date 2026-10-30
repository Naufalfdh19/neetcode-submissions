class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0
        n = len(s)
        result = 0
        while r < n:
            if s[r] not in seen:
                seen.add(s[r])
            else:
                if result < r-l:
                    result = r-l

                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
            
            r += 1
        
        return max(result, r-l)

