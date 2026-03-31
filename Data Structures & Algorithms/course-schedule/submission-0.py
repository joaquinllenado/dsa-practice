class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_to_prereqs = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            course_to_prereqs[course].append(prereq)

        visited = set()
        
        def dfs(c):
            if c in visited:
                return False
            if course_to_prereqs[c] == []:
                return True

            visited.add(c)
            for prereq in course_to_prereqs[c]:
                if not dfs(prereq):
                    return False
            
            visited.remove(c)
            course_to_prereqs[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True