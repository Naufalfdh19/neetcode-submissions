class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        def backtrack(i, bucket, total):
            if total == target:
                res.append(bucket.copy())
                return
            
            if total > target or i >= len(candidates):
                return

            backtrack(i+1, bucket+[candidates[i]], total+candidates[i])


            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, bucket, total)

        backtrack(0,[],0)


        return res
