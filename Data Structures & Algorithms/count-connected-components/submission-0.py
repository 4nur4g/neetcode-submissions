class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_map = {i:[] for i in range(n)}
        for a, b in edges:
            adj_map[a].append(b)
            adj_map[b].append(a)
        visited = set()
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for adj in adj_map[node]:
                dfs(adj)
        count = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1 
        return count
        