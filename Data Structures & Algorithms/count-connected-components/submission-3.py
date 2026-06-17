class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent_arr = [i for i in range(n)]
        compo = n
        def find_root(node):
            while parent_arr[node] != node:
                node = parent_arr[node]
            return node
            
        for a,b in edges:
            root_a = find_root(a)
            root_b = find_root(b)
            if not root_a == root_b:
                parent_arr[root_a] = root_b
                compo -= 1
        return compo
            



        