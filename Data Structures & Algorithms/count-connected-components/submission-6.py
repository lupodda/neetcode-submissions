class Dsu:
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1]*n
        self.components = n

    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)

        if root1 != root2:
            self.components -= 1

        if self.sizes[root1]> self.sizes[root2]:
            self.parents[root2] = root1
            self.sizes[root1] += self.sizes[root2]
        else:
            self.parents[root1] = root2
            self.sizes[root2] += self.sizes[root1]

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = Dsu(n)

        for a, b in edges:
            dsu.union(a,b)

        return dsu.components
        