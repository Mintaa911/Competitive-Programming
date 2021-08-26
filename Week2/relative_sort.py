def relativeSortArray(arr1,arr2):
        c = []
        for x in arr2:
            i = 0
            while i < len(arr1):
                if arr1[i] == x:
                    c.append(x)
                    arr1.pop(i)
                else:
                    i += 1
        for x in range(1,len(arr1)):
            cur = arr1[x]
            y = x
            while y > 0 and arr1[y-1] > cur:
                arr1[y] = arr1[y-1] 
                y -= 1
            arr1[y] = cur
        [c.append(x) for x in arr1]
        return c
