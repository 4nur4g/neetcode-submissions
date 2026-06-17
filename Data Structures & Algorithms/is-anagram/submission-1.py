class Solution:
    def return_counts(self, s: str):
        count = {}
        for char in s:
            count[char] = count.get(char,0) + 1
        return count
        
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = self.return_counts(s)
        count2 = self.return_counts(t)
        return count1 == count2
        
        