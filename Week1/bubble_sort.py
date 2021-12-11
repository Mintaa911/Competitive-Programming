def bubble_sort(a):
    swap = 0 
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                swap += 1
                a[j],a[j+1] = a[j+1],a[j]
    print(f'Array is sorted in {swap} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
