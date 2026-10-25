class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0

        maxSubstring = -1
        duplicateCheck = {}

        while r < len(s):
            if s[r] not in duplicateCheck:
                duplicateCheck[s[r]] = True
            else:
                if maxSubstring < r-l:
                    maxSubstring = r-l
                while s[l] != s[r]:
                    del duplicateCheck[s[l]]
                    l += 1
                l += 1
            r += 1

        if maxSubstring < r-l:
            maxSubstring = r-l
        
        return maxSubstring