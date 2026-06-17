class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Edge case checks
        if not nums or k == 0:
            return []
        
        left = 0
        res = []
        q = collections.deque()  

        for right in range(len(nums)):
            num = nums[right]
            while q and num > nums[q[-1]]:
                q.pop()
            q.append(right)
            if right - left + 1 == k:
                maxVal = nums[q[0]]  
                res.append(maxVal)
                left += 1
                if q and q[0] < left:
                    q.popleft()

        
        return res

            
        
        