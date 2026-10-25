class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(2000)]
        hashmap = defaultdict(int)
        
        for num in nums:
            hashmap[num] += 1
        
        for key, value in hashmap.items():
            bucket[value].append(key)

        result = []

        pointer = len(bucket)-1
        while k > 0:
            for i in range(len(bucket[pointer])):
                if k > 0:
                    result.append(bucket[pointer][i])
                k -= 1

            pointer -= 1

        return result

