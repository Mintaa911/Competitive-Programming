class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        dependency = defaultdict(list)
        q = deque()
        
        for c1,c2 in prerequisites:
            indegree[c1] += 1
            dependency[c2].append(c1)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        stack = []
        while q:
            course = q.popleft()
            stack.append(course)
            for c in dependency[course]:
                indegree[c] -= 1
                
                if indegree[c] == 0:
                    q.append(c)
        
        return stack if len(stack) == numCourses else []
