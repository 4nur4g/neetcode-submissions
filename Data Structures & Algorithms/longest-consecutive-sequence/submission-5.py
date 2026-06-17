class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        u_nums = set(nums)
        max_range = 1

        for num in u_nums:
            cur_range = 1
            # seq start or not
            if num-1 in u_nums:
                continue
            length = 1
            while num + length in u_nums:
                length += 1
            max_range = max(max_range, length)
        return max_range

        

            

        