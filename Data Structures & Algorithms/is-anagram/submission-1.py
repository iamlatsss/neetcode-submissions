class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = []
        list2 = []
        for i in range(len(s)):
            list1.append(s[i])
        for j in range(len(t)):
            list2.append(t[j])
        
        if sorted(list1) == sorted(list2):
            return True
        return False