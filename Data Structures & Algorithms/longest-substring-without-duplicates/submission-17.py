class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l = 0 
        r = 1
        res = 0
        track = set([s[0]])
        while r < len(s):
            if s[r] not in track:
                track.add(s[r])
                res = max(res,r-l+1)
                r += 1
                continue
            while s[r] in track:
                track.remove(s[l])
                l += 1
        return res
            

        