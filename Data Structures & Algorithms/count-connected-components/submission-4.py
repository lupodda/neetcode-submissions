class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)

        if root_a == root_b:
            return 0
        
        if self.size[root_a]<= self.size[root_b]:
            self.parent[root_b] = root_a
            self.size[root_a] += self.size[root_b]

        else:
            self.parent[root_a] = root_b
            self.size[root_b] += self.size[root_a]
        
        return 1
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for a, b in edges:
            n -= dsu.union(a,b)

        return n
        