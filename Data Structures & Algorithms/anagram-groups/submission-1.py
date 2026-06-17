class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = collections.defaultdict(list)
        for word in strs:
            key = [i for i in range(27)]
            for c in word:
                key[ord(c)-ord('a')] += 1
            store[tuple(key)].append(word)
        return store.values()
        