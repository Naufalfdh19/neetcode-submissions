class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}

        for i, num in enumerate(nums):
            if num in sumMap:
                return [sumMap[num][1], i]
            sumMap[target-num] = [num, i]
