from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # convert the edge list in adjacency list
        # use the adjacency list to see which nodes have 0 incoming edges
        # Use in_degree array to store for each node the number of incoming edges
        # initialze a queue with the nodes woth 0 incoming edges
        # popleft from the queue and store the visited nodes
        # return numCourses == len(visited)
        graph = defaultdict(list)
        queue = deque()
        in_degree = [0]*numCourses
        visited = 0

        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a]+=1

        for node in range(numCourses):
            if in_degree[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            visited +=1
            for nei in graph[node]:
                in_degree[nei] -=1
                if in_degree[nei] == 0:
                    queue.append(nei)

        return numCourses == visited
                

        

        





        