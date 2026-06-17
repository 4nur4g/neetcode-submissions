class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        for w in strs:
            key = [0 for i in range(26)]
            for c in w:
                key[ord(c)-ord('a')] += 1
            if tuple(key) not in temp:
                temp[tuple(key)] = []
            temp[tuple(key)].append(w)
        return list(temp.values())
        