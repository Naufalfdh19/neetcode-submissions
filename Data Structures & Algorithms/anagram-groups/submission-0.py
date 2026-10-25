class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = []

        for string in strs:
            isNotMatching = True
            for i in range(len(group)):
                if self.isAnagram(string, group[i][0]):
                    group[i].append(string)
                    isNotMatching = False
                    break
                
            if isNotMatching:
                group.append([string])
        
        return group
                

    def isAnagram(self, s, t):
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
        