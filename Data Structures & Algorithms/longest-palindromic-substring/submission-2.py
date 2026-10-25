class Solution:

    def isPalindrome(self, a):
        return a == a[::-1]


    def longestPalindrome(self, s: str) -> str:
        l = 0
        maximumLength = 0
        res = ""
        while l < len(s):
            r = len(s)-1
            while l <= r:
                if s[l] == s[r]:
                    subString = s[l:r+1]
                    print(subString)
                    if self.isPalindrome(subString):
                        if len(subString) > maximumLength:
                            maximumLength = len(subString)
                            res = subString
                            break
                r -= 1
            l += 1
        
        return res
                

