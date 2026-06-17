class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        tempMap = collections.defaultdict(int)
        maxFreq = 0
        result = 0
        for index,letter in enumerate(s):
            tempMap[letter] += 1
            windowLen = index - left + 1 
            maxFreq = max(tempMap[letter], maxFreq)
            if windowLen - maxFreq > k:
                tempMap[s[left]] -= 1
                left += 1
        return index - left + 1

                


            


        