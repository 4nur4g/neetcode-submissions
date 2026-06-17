class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row iteration
        u_map, c_map = defaultdict(set), defaultdict(set)
        for r_ind, r in enumerate(board):
            r_set = set()
            for c_ind, c in enumerate(r):
                if c == ".":
                    continue
                if c in r_set:
                    return False
                if c in c_map[c_ind]:
                    return False
                co_ord = ((r_ind)//3,(c_ind)//3)
                if c in u_map[(co_ord)]:
                    return False
                u_map[co_ord].add(c)
                r_set.add(c)
                c_map[c_ind].add(c)
        return True
        