class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def hamming_distance_of_one(str1, str2):
            count = sum(c1 != c2 for c1, c2 in zip(str1, str2))
            if count == 1:
                return True
            return False

        def bfs(string):
            visited = set()
            dq = deque([string])
            ans = 0
            visited.add(string)
            while dq:
                ans += 1
                for i in range(len(dq)):
                    s1 = dq.popleft()
                    if s1 == endWord:
                        return ans
                    for s2 in adjList[s1]:
                        if s2 not in visited:
                            dq.append(s2)
                            visited.add(s2)
            return 0

        if endWord not in wordList: return 0
        adjList = defaultdict(set)
        wordList.append(beginWord)
        for s1 in wordList:
            for s2 in wordList:
                if s1 == s2:
                    continue
                if hamming_distance_of_one(s1, s2):
                    adjList[s1].add(s2)
                    adjList[s2].add(s1)

        return bfs(beginWord)
