class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj_map = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj_map[pattern].append(word)
        q = collections.deque([beginWord])
        visited = set([beginWord])
        layer = 0
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return layer + 1
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neighbor in adj_map[pattern]:
                        if neighbor not in visited:
                            q.append(neighbor)
                            visited.add(neighbor)
            layer += 1
        return 0

        