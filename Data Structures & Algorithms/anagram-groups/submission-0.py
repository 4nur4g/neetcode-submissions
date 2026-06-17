class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ansObject
        ans = collections.defaultdict(list)
        for word in strs:
            freq = [0]*26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            ans[tuple(freq)].append(word)
        return ans.values()

        