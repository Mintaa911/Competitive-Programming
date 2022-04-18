class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:    
        def makeStore(data):
            store = defaultdict(list)
            owner = dict()
            for acc in data:
                for i in range(1,len(acc)):
                    if acc[i] not in store:
                        store[acc[i]].append(acc[i])
                        store[acc[i]].append(1)
                        owner[acc[i]] = acc[0]
            return [store,owner]
        
        def find(node,store):
            if node == store[node][0]:
                return store[node]
            store[node] = find(store[node][0],store) 
            return store[node]
        
        def union(e1,e2,store):
            root_e1 = find(e1,store)
            root_e2 = find(e2,store)
            if root_e1 != root_e2:
                if root_e1[1] > root_e2[1]:
                    root_e1,root_e2 = root_e2,root_e1      
                root_e1[0] = root_e2[0]
                root_e2[1] += root_e1[1]
        
        store,owner = makeStore(accounts)     
        for acc in accounts:
            for i in range(1,len(acc)-1):
                union(acc[i],acc[i+1],store)             
                
        emails = defaultdict(list)
        for ky,val in store.items():
            parent = find(ky,store) 
            emails[parent[0]].append(ky)
            
        res = [] 
        for ky,val in emails.items():
            val.sort()
            temp = [owner[ky]]
            temp.extend(val)
            res.append(temp)
        
        return res
