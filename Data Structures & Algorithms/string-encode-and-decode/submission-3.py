class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += string
            res += "-"

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        subString = ""
        for char in s:
            if char == "-":
                res.append(subString)
                subString = ""
            else:
                subString += char
            
        return res