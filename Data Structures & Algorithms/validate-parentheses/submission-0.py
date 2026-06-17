class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)% 2 != 0 or s == "":
            return False
        closeMap = {"{":"}","(":")","[":"]"}
        openBrack = closeMap.keys()
        q = collections.deque()
        for char in s: 
            if char in openBrack:
                q.append(char)
            else:
                if not q or closeMap[q[-1]] != char:
                    return False
                q.pop()
        return not q

        