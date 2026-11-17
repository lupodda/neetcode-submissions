from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]* numCourses
        graph = defaultdict(list)
        queue = deque()
        taken_courses = []

        for a, b in prerequisites:
            indegree[a]+=1
            graph[b].append(a)
        
        for node, degree in enumerate(indegree):
            if degree == 0:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            taken_courses.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return taken_courses if len(taken_courses) == numCourses else []
                
