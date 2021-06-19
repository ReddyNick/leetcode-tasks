import collections

class Solution:       
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        deque = collections.deque([0])
        visited = [False] * (len(s) + 1)
        while deque:
            start = deque.popleft()
            for end in range(start + 1, len(s) + 1):
                if not visited[end] and s[start:end] in wordDict:
                    if end == len(s):
                        return True
                    visited[end] = True
                    deque.append(end)
                    
                    
        return False
