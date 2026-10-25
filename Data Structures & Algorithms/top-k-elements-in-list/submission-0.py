class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}

        for num in nums:
            if num not in countMap:
                countMap[num] = 0
            countMap[num] += 1
        
        countList = sorted(countMap.items(), key=lambda x:x[1], reverse=True)

        return [countList[i][0] for i in range(k)]