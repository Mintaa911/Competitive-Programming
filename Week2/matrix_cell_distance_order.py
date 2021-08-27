class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        metrix = [[x,y] for x in range(rows) for y in range(cols)]
        arr2d = []
        for cell in metrix:
            distance = abs(rCenter-cell[0]) + abs(cCenter-cell[1])
            arr2d.append([distance,cell])

        arr = self.quick_sort(arr2d,0,(len(arr2d)-1))
            
        return [x[1] for x in arr]
    
    def quick_sort(self,arr,l,h):
        if l >= h:
            return 
        p = self.partition(arr,l,h)
        self.quick_sort(arr,l,p-1)
        self.quick_sort(arr,p+1,h)
        return arr
                                
    def partition(self,arr,l,h):
        pivot = arr[h]
        j = l -1
        for i in range(l,h):
            if arr[i][0] < pivot[0]:
                j += 1
                arr[i],arr[j] = arr[j],arr[i]       
        arr[h],arr[j+1] = arr[j+1],arr[h]
        return j + 1
