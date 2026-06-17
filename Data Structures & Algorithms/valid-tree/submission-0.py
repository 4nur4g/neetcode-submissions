class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj_map = {i:[] for i in range(n)}
        for a,b in edges:
            adj_map[a].append(b)
            adj_map[b].append(a)
        
        visited = set()
        def dfs(n, last):
            if n in visited:
                return False
            visited.add(n)
            for node in adj_map[n]:
                if node == last:
                    continue
                if not dfs(node, n):
                    return False
            return True

        return dfs(0,-1) and len(visited) == n

        