class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(bucket, total):
            if len(bucket) == 2*n:
                if total == 0:
                    res.append(bucket)
                return
            
            if total == -1:
                return
            

            backtrack(bucket+"(", total+1)
            backtrack(bucket+")", total-1)

        backtrack("",0)

        return res
