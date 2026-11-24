class Dsu:
    def __init__(self, n):
        self.parent=list(range(n))
        self.size=[1]*n
        self.components = n 
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 != root2:
            self.components -=1

        if self.size[root1] > self.size[root2]:
            self.parent[root2] = self.parent[root1] 
            self.size[root1] += self.size[root2]

        else:
            self.parent[root1] = self.parent[root2]
            self.size[root2] += self.size[root1] 


    


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        dsu = Dsu(n)

        for a,b in edges:
            dsu.union(a,b)
        
        return dsu.components


        