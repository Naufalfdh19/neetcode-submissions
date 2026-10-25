class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap = {}

        for char in s:
            if char not in charMap:
                charMap[char] = 0
            charMap[char] += 1
        
        for char in t:
            if char not in charMap:
                return False

            charMap[char] -= 1
            if charMap[char] == 0:
                del charMap[char]
  
        return True if len(charMap) == 0 else False