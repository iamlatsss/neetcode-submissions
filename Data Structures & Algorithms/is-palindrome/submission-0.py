class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''

        for i in s:
            if i.isalnum():
                res += i.lower()
        resrev = res[::-1]
        return res == resrev
