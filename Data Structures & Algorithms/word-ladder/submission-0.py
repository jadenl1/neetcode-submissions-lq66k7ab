from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        graph = defaultdict(set)
            
        def defineEdge(aWord, bWord):
            diff = 0
            for i in range(len(aWord)):
                if aWord[i] != bWord[i]:
                    diff += 1
            if diff == 1:
                graph[aWord].add(bWord)
                graph[bWord].add(aWord)
        
        wordList.append(beginWord)
        n = len(wordList)

        for i in range(n):
            for j in range(i, n):
                defineEdge(wordList[i], wordList[j])
        
        print(graph)

        # now BFS from start -> end
        q = deque()
        visited = set()
        q.append(beginWord)
        distance = 1

        while q:
            # drain the q
            qLen = len(q)
            for i in range(qLen):
                curr = q.popleft()
                visited.add(curr)

                if curr == endWord:
                    return distance

                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        q.append(neighbor)
            distance += 1

        return 0