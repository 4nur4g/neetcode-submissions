class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        win_size = len(s1)
        l = 0
        track = Counter()
        for r in range(len(s2)):
            track[s2[r]] += 1
            if r - l + 1 > win_size:
                track[s2[l]] -= 1
                l += 1
            if r - l + 1 == win_size and track == s1_counter:
                return True
        return False

        