class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash1 = defaultdict(list)
        for i in strs:
            sortstr = "".join(sorted(i))
            hash1[sortstr].append(i)
        return list(hash1.values())