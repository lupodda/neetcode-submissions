class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1)) # {} for strings but we have to initailize it before
        self.size = [1]*(n+1)

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)

        if root_a == root_b:
            return False

        if self.size[root_a] >= self.size[root_b]:
            self.size[root_a] += self.size[root_b]
            self.parent[root_b] = self.parent[root_a]
        else:
            self.size[root_b] += self.size[root_a]
            self.parent[root_a] = self.parent[root_b]

        return True
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))

        for a,b in edges:

            if not dsu.union(a,b):
                return [a,b]


    #MAIN TAKEAWAYS
    # I dont have a cycle untile i close it, so the last edge in the cylce is the one that satisfied the property
    # Always check the input, in this case is from 1 to n not from 0 to n-1
    # Always remember to use slef everywhere

    # Time complexity: O(v+e * alpha(v)) where alpha is the ackermann function
    #Space : O(2v)

        #     n = len(edges)
        # parent = list(range(n + 1))
        # def find(node):
        #     if node != parent[node]:
        #         parent[node] = find(parent[node])
        #     return parent[node]
        # for a, b in edges:
        #     root_a, root_b = find(a), find(b)
        #     if root_a == root_b:
        #         return [a, b]
        #     parent[root_b] = root_a



        