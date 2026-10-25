class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prevNums = nums.copy()
        n = len(nums)
        nums[0] = 1
        total = prevNums[0]
        for i in range(1, n):
            nums[i] = total
            total *= prevNums[i]

        total = prevNums[-1]
        for i in range(n-2,-1,-1):
            nums[i] = nums[i]*total
            total *= prevNums[i]

        return nums
