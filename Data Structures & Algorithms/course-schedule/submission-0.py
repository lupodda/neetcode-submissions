from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0]*numCourses
        for a, b in prerequisites: 
            graph[b].append(a)
            in_degree[a]+=1
        
        queue = deque()
        processed = 0

        for node in range(numCourses):
            if in_degree[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            processed += 1
            for exam in graph[node]:
                in_degree[exam] -= 1
                if in_degree[exam] == 0:
                    queue.append(exam)
        
        return processed == numCourses 

            


                


                
                



