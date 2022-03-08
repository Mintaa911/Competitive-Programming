class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        q = deque([beginWord])
        visited = set()
        count = 1
        while q:
            length_q = len(q)
            for i in range(length_q):
                popped = q.popleft()
                if popped == endWord:
                    return count
                if popped in visited:
                    continue
                visited.add(popped)
                for i in range(len(popped)):
                    for j in range(26):
                        c = chr(97 + j)
                        word = popped[0:i] + c + popped[i+1:]
                        if word in visited:
                            continue
                        if word in wordSet:
                            q.append(word)
                            wordSet.remove(word)
            count +=1
        
        return 0
