class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        part2 = sum(nums)
        dp = [part2]*n

        if part2 % 2 != 0:
            return False

        for i in range(n):
            pointer = i
            while pointer < n:
                dp[i] -= nums[pointer]
                if dp[i] < part2//2:
                    dp[i] += nums[pointer]
                if dp[i] == part2//2:
                    return True
                pointer += 1

           
            

        return False