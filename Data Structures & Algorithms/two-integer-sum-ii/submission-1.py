class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(numbers)

        for i in range(n):
            num = numbers[i]
            if target-num in hashmap:
                return [hashmap[target-num]+1,i+1]

            hashmap[num] = i

        return []