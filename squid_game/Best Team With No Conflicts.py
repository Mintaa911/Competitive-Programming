class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = []
        for i in range(len(scores)):
            pairs.append([scores[i],ages[i]])
        pairs.sort(reverse=True)
        
        res = self.helper(0,pairs,float('inf'),{})
        return res

    def helper(self,idx,pairs,younger,memo):
        if idx == len(pairs):
            return 0
        if (idx,younger) in memo:
            return memo[(idx,younger)]
        score,age = pairs[idx]
        res = 0
        if age <= younger:
            pick = self.helper(idx+1,pairs,min(younger,age),memo) + score
            res = max(res,pick)            
        not_pick = self.helper(idx+1,pairs,younger,memo)
        res = max(res,not_pick)
        memo[(idx,younger)] = res
        return memo[(idx,younger)]
