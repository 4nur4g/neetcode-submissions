class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = set()
        l = 0
        res = 0

        # Straight forward code
        
        for r in range(len(s)):
            # If we hit a duplicate, shrink the window from the left
            while s[r] in track:
                track.remove(s[l])
                l += 1
                
            # Add the current character and update the max length
            track.add(s[r])
            res = max(res, r - l + 1)
            
        return res