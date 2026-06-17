class Solution:
    def get_ind(self,char):
        return ord(char) - 97
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_c = [0] * 26
        for c in s1:
            s1_c[self.get_ind(c)] += 1
        l = 0
        for r in range(len(s1)-1,len(s2)):
            comp = [0] * 26
            for c in s2[l:r+1]:
                comp[self.get_ind(c)] += 1
            if comp == s1_c:
                return True
            l += 1
        return False
        