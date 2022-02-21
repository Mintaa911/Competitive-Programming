class Solution:
        #Heapify function to maintain heap property.
    def upHeap(self,arr,i):
        p = self.parent(i)
        
        while p >= 0 and  arr[i] > arr[p]:
            arr[i],arr[p] = arr[p],arr[i]
            i = p
            p = self.parent(i)
       
    def downHeap(self,arr,n,i):
        lg = i
        l,r = self.leftChild(i),self.rightChild(i)
        
        if l < n and arr[l] > arr[lg]:
            lg = l
        if r < n and arr[r] > arr[lg]:
            lg = r
        if lg != i:
            arr[lg],arr[i] = arr[i],arr[lg]
            self.downHeap(arr,n,lg)
        
    def heapify(self,arr, n, i):
        # code here
        self.upHeap(arr,i)
        self.downHeap(arr,n,i)
        
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        l = len(arr)//2 -1
        for i in range(l,-1,-1):
            self.downHeap(arr,n,i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr,n)
        startIdx = len(arr)-1
        for i in range(startIdx,0,-1):
            arr[0],arr[i] = arr[i],arr[0]
            self.downHeap(arr,i,0)
        
        
    def insert(self,arr,element):
        arr.append(element)
        self.upHeap(arr,len(arr)-1)
       
    def remove(self,arr,idx):
        l = len(arr)
        arr[idx],arr[l-1] = arr[l-1],arr[idx]
        arr.pop()
        self.heapify(arr,l-1,idx)
       
        
    def update(self,arr,idx,val):
        arr[idx] = val
        p = self.parent(idx)
        
        if arr[idx] < arr[p]:
            self.downHeap(arr,len(arr),idx)
        else:
            self.upHeap(arr,idx)
            
       
        
    
    def getMax(self,arr):
        return arr[0]
       
        
    def leftChild(self,idx):
        return 2 * idx + 1
        
    def rightChild(self,idx):
        return 2 * idx + 2
        
    def parent(self,idx):
        return idx//2

