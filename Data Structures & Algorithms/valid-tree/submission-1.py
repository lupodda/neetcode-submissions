from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False 
        
        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        queue = deque([(0, -1)])
        visited = set()
        while queue:
            node, parent = queue.popleft()
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                    
                if neighbor in visited:
                    return False

                visited.add(neighbor)
                queue.append((neighbor, node))

        return len(visited) == n
        






        # graph = defaultdict(list)
        # for a, b in edges:


       
        #            0        2           0
        #          1   2     3  1         1 3      2
        #        2   4        0 4       3         4
        #      3

        # MAIN TAKEAWAY
        # trees have n node and n-1 edges