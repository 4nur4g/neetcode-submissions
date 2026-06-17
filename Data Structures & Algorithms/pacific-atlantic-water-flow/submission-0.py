class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        visit_pacific, visist_atlantic = set(), set()
        def dfs(r,c,lastHeight,visited_set):
            if (r,c) not in visited_set and r in range(ROWS) and c in range(COLS) and heights[r][c] >= lastHeight:
                visited_set.add((r,c))
                dirs = [(1,0),(-1,0),(0,1),(0,-1)]
                for ra, ca in dirs:
                    dfs(r + ra, c + ca, heights[r][c], visited_set)
        for c in range(COLS):
            dfs(0,c,heights[0][c],visit_pacific)
            dfs(ROWS-1,c,heights[ROWS-1][c],visist_atlantic)
        for r in range(ROWS):
            dfs(r,0,heights[r][0],visit_pacific)
            dfs(r,COLS-1,heights[r][COLS-1],visist_atlantic)
        common = visit_pacific & visist_atlantic
        return [list(item) for item in common]


        

        