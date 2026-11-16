class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        has1 = defaultdict(int)
        has2 = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in s:
            has1[i] += 1
        for i in t:
            has2[i] += 1

        return has1 == has2

