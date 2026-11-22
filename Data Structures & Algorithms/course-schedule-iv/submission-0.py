from collections import defaultdict, deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegree = [0]*numCourses
        graph = defaultdict(list)
        is_prereq= defaultdict(set)
        queue = deque()
        answers = [False]*len(queries)

        for a, b in prerequisites:
            indegree[b]+=1
            graph[a].append(b)
        
        for i, degree in enumerate(indegree):
            if degree == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                is_prereq[nei].add(node)
                is_prereq[nei].update(is_prereq[node])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        for i, (u, v) in enumerate(queries):
            if u in is_prereq[v]:
                answers[i] = True

        return answers

    
        