class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedS = "".join(s.split())

        l, r = 0, len(cleanedS)-1

        while l < r:
            if not cleanedS[l].isalnum():
                l += 1
                continue
            if not cleanedS[r].isalnum():
                r -= 1
                continue
            if cleanedS[l].lower() != cleanedS[r].lower():
                return False

            l += 1
            r -= 1

        return True
