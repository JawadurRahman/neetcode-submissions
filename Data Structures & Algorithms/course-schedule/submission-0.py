class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqmap = defaultdict(set)
        for course, course_prereq in prerequisites:
            prereqmap[course].add(course_prereq)

        visited = set()
        completed = set()
        def dfs(course):
            if course in completed: return True
            if course in visited: return False

            visited.add(course)
            for prereq in prereqmap[course]:
                if dfs(prereq) == False:
                    return False
            
            visited.remove(course)
            completed.add(course)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        

        return True