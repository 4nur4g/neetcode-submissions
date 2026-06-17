class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        r = 0
        l = 0
        track = defaultdict(int)
        res = 0
        for r in range(len(s)):
            track[s[r]] += 1
            while r - l + 1 - max(track.values()) > k:
                track[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res



        