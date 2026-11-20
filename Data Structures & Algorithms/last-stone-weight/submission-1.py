import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        stack = []

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            
            diff = stone1-stone2

            if diff != 0:
                heapq.heappush(stones, diff)

        return -stones[0] if stones else 0
        