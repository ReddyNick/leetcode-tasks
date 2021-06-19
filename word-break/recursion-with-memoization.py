class Solution:       
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [None] * len(s)
        return self.recf(0, s, wordDict, memo)
    
    def recf(self, start, s, wordDict, memo):
        if start == len(s):
            return True 
        
        if memo[start] is not None:
            return memo[start]
        
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordDict and self.recf(end, s, wordDict, memo):
                memo[start] = True
                return True
        
        memo[start] = False
        return False
