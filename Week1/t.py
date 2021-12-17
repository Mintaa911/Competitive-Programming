from collections import Counter
def t(changed):
    ans = []
    changed = sorted(changed)
    freq = Counter(changed)

    for num in changed:

        if freq[num] == 0:
            continue

        if freq[num*2] == 0:
            return []

        if num == 0 and freq[num] <= 1:
            return []

        ans.append(num)
        freq[num] -= 1
        freq[num*2] -= 1
    return ans

print(t([0,0]))