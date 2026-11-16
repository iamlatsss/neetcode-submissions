class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        has = {"{" : "}", "(" : ")", "[" : "]"}
        for i in s:
            if i in has:
                res.append(i)
            else:
                if not res or has[res[-1]] != i:
                    return False
                res.pop()
        
        return not res