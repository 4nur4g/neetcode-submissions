class Solution:
    def jump(self, nums: List[int]) -> int:
        q = collections.deque([(0,nums[0])])
        min_jumps = 0
        visited = set((0,nums[0]))
        while q:
            for _ in range(len(q)):
                ind, jumps = q.popleft()
                if ind == len(nums) - 1:
                    return min_jumps
                for j in range(1,jumps+1):
                    if j + ind < len(nums) and (j+ind, nums[j+ind]) not in visited:
                        q.append((j+ind, nums[j+ind]))
                        visited.add((j+ind, nums[j+ind]))
            min_jumps += 1
        return min_jumps
                
             
            
        