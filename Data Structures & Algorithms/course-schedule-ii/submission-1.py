from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0]*numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a]+=1
        
        queue = deque()

        for node in range(numCourses):
            if in_degree[node] == 0:
                queue.append(node)

        valid_ordering = []

        while queue:
            node = queue.popleft()
            valid_ordering.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor]-=1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return valid_ordering if len(valid_ordering) == numCourses else []




        