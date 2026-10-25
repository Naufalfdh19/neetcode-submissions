class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            sortedWord = "".join(sorted(word))
            hashmap[sortedWord].append(word)

        result = []

        for _, value in hashmap.items():
            result.append(value)


        return result

        
            