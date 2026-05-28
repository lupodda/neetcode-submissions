class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph= defaultdict(list)
        in_degree=[0]*numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a]+=1

        queue=deque()
        processed=0

        for c in range(numCourses):
            if in_degree[c]==0:
                queue.append(c)

        while queue:
            course =queue.popleft()
            processed+=1
            for nei in graph[course]:
                in_degree[nei]-=1
                if in_degree[nei]==0:
                    queue.append(nei)

        return processed==numCourses

        
        