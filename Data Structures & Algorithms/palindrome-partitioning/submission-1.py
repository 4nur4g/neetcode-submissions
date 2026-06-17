class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sub, res = [], []
        size = len(s)
        def backtrack(i):
            if i >= size:
                res.append(sub.copy())
            for j in range(i,size):
                if self.is_pal(s,i,j):
                    sub.append(s[i:j+1])
                    backtrack(j+1)
                    sub.pop()
        backtrack(0)
        return res
        
    def is_pal(self, s, i,j):
        if s[i] != s[j]:
            return False
        l, r = i, j

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True