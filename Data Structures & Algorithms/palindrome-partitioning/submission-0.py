class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pallindrome(i,j):
            sub_string = s[i:j+1]
            if sub_string[0] != sub_string[-1]:
                return False
            l,r = 0,len(sub_string)-1
            while l<r:
                if sub_string[l] != sub_string[r]:
                    return False
                l+=1
                r-=1
            return True
        res, track = [],[]
        def backtrack(i):
            if i >= len(s):
                res.append(track.copy())
                return
            for j in range(i,len(s)):
                if is_pallindrome(i,j):
                    track.append(s[i:j+1])
                    backtrack(j+1)
                    track.pop()
        backtrack(0)
        return res

            
        