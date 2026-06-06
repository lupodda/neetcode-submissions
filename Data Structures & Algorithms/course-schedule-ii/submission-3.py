from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #TOPOLOGICAL SORTING!!!!!
        # USE IN_DEGREE!!!
        # convert the edge list in adjacency list
        # initialize a q with 0 but we could start from whatever node
        # initialize a visited set with 0
        # pop from the queue and add the node to the res array
        # visit  the neighbors
        # add the neighbors to the queue
        # return the res array if len(visited) == nunmCourses else []

        graph = defaultdict(list)
        indegree = [0]*numCourses
        queue = deque()
        res = []

        
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        
        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            res.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return res if len(res) == numCourses else []


        