from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree= [0]*numCourses
        graph = defaultdict(list)
        queue = deque()

        for a, b in prerequisites:
            indegree[a]+=1
            graph[b].append(a)
        
        for node, degree in enumerate(indegree):
            if degree == 0:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            numCourses -= 1

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return numCourses == 0

        #MAIN TAKEAWAYS
        # draw a graph whenever I strugggle with direction of edges and in general helps to reason on the problem
        # as soon as I see prerequisites I should think of Kahn algo or topological sorting
        
        # Time and space complexity:
        # time and space: O(V+E)


