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
        visited = set({0})
        while queue:
            node, parent = queue.popleft()
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                    
                if neighbor in visited:
                    return False

                visited.add(neighbor)
                queue.append((neighbor, node))

        return len(visited) == n

        # MAIN TAKEAWAY
        # trees have n node and n-1 edges
        # even when len(edges) == n-1 we need to check for loops and disconnected graphs
        # when we know the basics we can focuse on the details. 
        # basics like: bfs implementation, difference between treed and graphs, convert edge list in adjacency list are a MUST!!
        # important to pass the parent because we are gonna loose this info at the next step
        # important to think at each node who is the parent and who are the neighbors
        # for the parent basecase giveing -1 as we have node with values form 0 to n-1
        # we cannot use in_degree properties because we have undirected graphs