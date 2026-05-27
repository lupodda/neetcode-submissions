class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!= n-1:
            return False

        graph=defaultdict(list)
        queue=deque([(0,-1)])
        visited=set({0})

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        while queue:
            node, parent = queue.popleft()
            for nei in graph[node]:
                if nei==parent:
                    continue 
                
                if nei in visited:
                    return False
                
                queue.append((nei,node))
                visited.add(nei)

        return len(visited)==n
        


        
    