class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # Bottom up approach
        
        # perms = [[]]
        
        # for num in nums:
        #     new_perms = []
        #     for perm in perms:
        #         for i in range(len(perm)+1):
        #             perm_copy = perm.copy()
        #             perm_copy.insert(i,num)
        #             new_perms.append(perm_copy)
        #     perms = new_perms

        # return perms

        # Top down approach

        if nums == []:
            return [[]]
        perms = self.permute(nums[1:])
        new_perms = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i,nums[0])
                new_perms.append(p_copy)
        return new_perms


















