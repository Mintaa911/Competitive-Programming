class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        def makeStore(n):
            store = defaultdict(int)
            for i in range(n):
                store[i] = [i,1]
            return store
        
        def findProvince(x,store):
            if x == store[x][0]:
                return store[x]
            
            store[x] = findProvince(store[x][0],store)
            return store[x]
        
        def mergeProvince(i,j,store):
           
            a = findProvince(i,store)
            b = findProvince(j,store)
          
            if a != b:
                if a[1] > b[1]:
                    a,b = b,a   
                a[0] = b[0]
                a[1] -= 1
                b[1] += 1
            

        
        store = makeStore(n)
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] == 1:
                    x = mergeProvince(i,j,store)
        
                    
        province = 0
        
        for ky,val in store.items():
            if ky == val[0]:
                province += 1
            
        return province
