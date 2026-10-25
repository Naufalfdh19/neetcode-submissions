class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1

        while l <= r:
            mid = l+(r-l)//2
            if matrix[mid][0] > target:
                r = mid-1
            elif matrix[mid][0] < target:
                l = mid+1
            else:
                return True

        nums = matrix[min(l,r)]

        l, r = 0, len(nums)-1

        while l <= r:
            mid = l+(r-l)//2

            if nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
            else:
                return True
    
        return False
