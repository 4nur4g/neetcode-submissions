class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = 0
        r = 0

        track = set()
        res = 0

        while r < len(s):
            if r == 0:
                track.add(s[r])
                res += 1
                r += 1
                continue
            while s[r] in track:
                track.remove(s[l])
                l += 1
            track.add(s[r])
            res = max(res,r-l+1)
            r += 1

        return res
                





        