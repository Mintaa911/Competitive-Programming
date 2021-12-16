def frequent(nums,k):
    nums.sort(reverse = True)
    freq = 0
    l, r = 0, 0
    while r < len(nums):
        k -= nums[l] - nums[r]
        while k < 0:
            k += (r - l) * (nums[l] - nums[l + 1])
            l += 1
            
        r += 1
        freq = max(freq, r - l)
    return freq

            
            