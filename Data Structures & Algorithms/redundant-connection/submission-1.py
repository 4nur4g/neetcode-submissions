class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [0 for i in range(len(edges) + 1)]
        # With Path Compression
        def find_root(node):
            if parent[node] != node:
                parent[node] = find_root(parent[node])
            return parent[node]
        for a,b in edges:
            root_a = find_root(a)
            root_b = find_root(b)
            if root_a == root_b:
                return [a,b]
            
            if rank[root_a] > rank [root_b]:
                parent[root_b] = root_a
            elif rank[root_a] < rank [root_b]: 
                parent[root_a] = root_b
            else:
                parent[root_a] = root_b
                rank[root_b] += 1

            
        


        