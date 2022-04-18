class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        def validCell(i,j):
            return i >= 0 and i < m and j >= 0 and j < n

          
        def makeStore(grid):
            store = defaultdict(list)
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        store[(i,j)].extend([[i,j],[1]])
            
            return store
        
        
        def find(i,store):
            if i == tuple(store[i][0]):
                return store[i]
            d = tuple(store[i][0])
            
            store[i] = find(d,store)
            
            return store[i]
        
        
        
        def union(a,b,store):
            if not validCell(b[0],b[1]):
                return
            if grid[b[0]][b[1]] == 0:
                return 
            
            root_a = find(a,store)
            root_b = find(b,store)
            
            if root_a != root_b:
                if root_a[1][0] > root_b[1][0]:
                    root_a, root_b = root_b,root_a
                
                root_a[0] = root_b[0]
            
                root_b[1][0] += root_a[1][0]
        
        store = makeStore(grid)
        m,n = len(grid), len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    union((i,j),(i,j+1),store)
                    union((i,j),(i,j-1),store)
                    union((i,j),(i-1,j),store)
                    union((i,j),(i+1,j),store)

        if [store[i][1][0] for i in store]:       
            return max([store[i][1][0] for i in store])
        else:
            return 0
            
