class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        closest = self.quick_sort(points,0,len(points)-1)
        return [points[x] for x in range(k)]
        
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
            d = sqrt((arr[i][0])**2 + (arr[i][1])**2)
            dPivot = sqrt((pivot[0])**2 + (pivot[1])**2)
            if d < dPivot:
                j += 1
                arr[i],arr[j] = arr[j],arr[i]       
        arr[h],arr[j+1] = arr[j+1],arr[h]
        return j + 1
