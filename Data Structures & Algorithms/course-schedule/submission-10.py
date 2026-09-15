from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = {}
        for i in range(numCourses):
            indegree[i] = 0

        graph = defaultdict(list)
        for a, b in prerequisites:
            # b -> a
            graph[b].append(a)
            indegree[a] += 1

        q = deque()
        for node, degree in indegree.items():
            if degree == 0:
                q.append(node)
        
        result = []
        while q:
            curr = q.popleft()
            result.append(curr)
            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        print(result)

        return len(result) == numCourses
