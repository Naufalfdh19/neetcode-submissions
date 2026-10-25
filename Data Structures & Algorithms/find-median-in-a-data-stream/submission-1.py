import heapq

class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.nums, num)

    def findMedian(self) -> float:
        numsCopy = self.nums.copy()
        if len(numsCopy) <= 1:
            return heapq.heappop(numsCopy)

        mid = len(numsCopy)//2
        
        for i in range(mid):
            first = heapq.heappop(numsCopy)

        second = heapq.heappop(numsCopy)

        if len(self.nums) % 2 == 0:
            return (first+second)/2
        return second