class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        maximumCount = 0

        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue

            if nums[i]-nums[i-1] != 1:
                if maximumCount < count:
                    maximumCount = count
                count = 0
                
            count += 1
        
        if maximumCount < count:
            maximumCount = count

        return maximumCount