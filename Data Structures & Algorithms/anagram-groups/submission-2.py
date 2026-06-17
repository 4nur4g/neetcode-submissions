class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for word in strs:
            store_key = [0]*26
            for c in word:
                store_key[ord(c)-ord('a')] += 1
            store[tuple(store_key)].append(word)
        return list(store.values())
