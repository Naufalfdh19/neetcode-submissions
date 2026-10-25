class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateMap = {}

        for num in nums:
            if num in duplicateMap:
                return True
            duplicateMap[num] = True
        
        return False