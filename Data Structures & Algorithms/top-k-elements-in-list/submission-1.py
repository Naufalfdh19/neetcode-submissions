class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1
        
        sortedItems = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)

        result = []

        idx = 0
        while k > 0:
            result.append(sortedItems[idx][0])
            k -= 1
            idx += 1
        
        return result

