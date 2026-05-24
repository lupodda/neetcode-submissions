from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 
        if len(edges) != n-1:
            return False
        
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        queue = deque([(0,-1)])
        visited = set({0})

        while queue:
            node, parent = queue.popleft()
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                if neighbor in visited:
                    return False

                queue.append((neighbor,node))
                visited.add(neighbor)

        return len(visited) == n

