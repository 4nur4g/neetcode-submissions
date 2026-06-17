class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        f_map = defaultdict(int)
        res = 0
        for r in range(len(s)):
            f_map[s[r]] += 1
            while r - l + 1 - max(f_map.values()) > k:
                f_map[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res     

        