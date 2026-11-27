class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        seen = set()

        nums.sort()

        def backtrack(i, bucket):
            seen.add(tuple(bucket))

            if i >= len(nums):
                return

            backtrack(i+1,bucket+[nums[i]])
            backtrack(i+1,bucket)


        backtrack(0,[])

        res = []

        for key in seen:
            res.append(list(key))

        return res
