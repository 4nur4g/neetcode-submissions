class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        tmap = Counter(t)
        tempMap = defaultdict(int)
        left = 0
        count = 0
        min_len = float('inf')
        min_window = ""
        
        for right in range(len(s)):
            letter = s[right]
            
            # If the current letter is in t, update the tempMap and count
            if letter in tmap:
                tempMap[letter] += 1
                if tempMap[letter] == tmap[letter]:
                    count += 1
            
            # When all characters are found, try to minimize the window
            while count == len(tmap):
                curr_len = right - left + 1
                if curr_len < min_len:
                    min_len = curr_len
                    min_window = s[left:right + 1]
                
                # Try to reduce the window size from the left
                if s[left] in tmap:
                    tempMap[s[left]] -= 1
                    if tempMap[s[left]] < tmap[s[left]]:
                        count -= 1
                left += 1
        
        return min_window


        