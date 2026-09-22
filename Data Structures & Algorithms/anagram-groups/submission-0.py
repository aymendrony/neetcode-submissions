class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictStr = defaultdict(list)
        Lists = []
        for s in strs:
            Tuple = tuple(sorted(s))
            if Tuple not in Lists:
                Lists.append(Tuple)
            dictStr[Tuple].append(s)
        return [dictStr[t] for t in Lists]
            