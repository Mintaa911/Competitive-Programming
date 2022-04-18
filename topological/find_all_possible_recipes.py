class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = defaultdict(int)
        dependency = defaultdict(list)
        
        for i in range(len(ingredients)):
            for ing in ingredients[i]:
                dependency[ing].append(recipes[i])
            
            indegree[recipes[i]] = len(ingredients[i])
                
        
        q = deque([supply for supply in supplies])
        
        while q:
            supply = q.popleft()
            
            for val in dependency[supply]:
                indegree[val] -= 1
                if indegree[val] == 0:
                    q.append(val)
                    
        ans = []
        
        for ky,val in indegree.items():
            if val == 0:
                ans.append(ky)
                
        return ans
