class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqmap = defaultdict(set)
        for course, course_prereq in prerequisites:
            prereqmap[course].add(course_prereq)

        visited = set()
        completed = set()
        ans = []
        def dfs(course):
            if course in completed: return True
            if course in visited: return False

            visited.add(course)
            for prereq in prereqmap[course]:
                if dfs(prereq) == False:
                    return False
            
            visited.remove(course)
            completed.add(course)
            ans.append(course)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []
        
        return ans