class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for x in strs:
            s+=x
            s+=";"
        return s
    def decode(self, s: str) -> List[str]:
        strs = s.split(";")
        return strs[:-1]

