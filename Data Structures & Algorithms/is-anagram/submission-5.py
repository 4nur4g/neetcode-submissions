class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = [0 for i in range(26)]
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            store[ord(s[i])-ord('a')] += 1
            store[ord(t[i])-ord('a')] -= 1
        return not any(store)
        