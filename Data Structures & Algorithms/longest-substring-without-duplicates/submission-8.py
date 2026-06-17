class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        right = 0
        tempSet = set()
        maxLen = 0
        while right < len(s):
            while s[right] in tempSet:
                tempSet.remove(s[left])
                left += 1
            tempSet.add(s[right])
            right += 1
            maxLen = max(maxLen, len(tempSet))
        return maxLen

        