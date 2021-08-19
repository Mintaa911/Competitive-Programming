def sockMerchant(n, ar):
    # Write your code here
    pair = 0
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
            if ar[i] == ar[j]:
                pair += 1
                ar.pop(j)
                break
    return pair
