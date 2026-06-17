class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_map = {}
        s2_map = {}
        for char in s1:
            s1_map[char] = s1_map.get(char,0) + 1
        left = 0
        for i in range(len(s1)):
            s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1
        for right in range(len(s1), len(s2)):
            if s1_map == s2_map:
                return True
            s2_map[s2[left]] -= 1
            if s2_map[s2[left]] == 0:
                del s2_map[s2[left]]
            left += 1
            s2_map[s2[right]] = s2_map.get(s2[right],0) + 1
        return s1_map == s2_map





                

        