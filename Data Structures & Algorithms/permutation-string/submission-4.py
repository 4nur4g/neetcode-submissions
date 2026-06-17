class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_c = {chr(i): 0 for i in range(97,97+26)}
        for c in s1:
            s1_c[c] += 1
        l = 0
        for r in range(len(s1)-1,len(s2)):
            comp = {chr(j): 0 for j in range(97,97+26)}
            for c in s2[l:r+1]:
                comp[c] += 1
            if comp == s1_c:
                return True
            l += 1
        return False
        