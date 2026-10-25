class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        return "?"+"zxz".join(strs)

    def decode(self, s: str) -> List[str]:
        if len(s) <= 0:
            return []

        return s[1:].split("zxz")
