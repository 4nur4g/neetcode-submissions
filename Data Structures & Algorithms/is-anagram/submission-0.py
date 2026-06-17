class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqMap1 = {}
        freqMap2 = {}
        for char in s:
            if char in freqMap1:
                freqMap1[char] += 1
            else: 
                freqMap1[char] = 1
        for char in t:
            if char in freqMap2:
                freqMap2[char] += 1
            else: 
                freqMap2[char] = 1
    
        return freqMap1 == freqMap2
         

        