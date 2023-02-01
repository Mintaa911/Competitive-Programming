class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        n = len(plantTime)
        pairs = []
        for i in range(n):
            pairs.append((growTime[i],plantTime[i]))

        pairs.sort(reverse=True)
        plant = 0
        blooms = 0
        idx = 0
        while idx < n:
            grow,plnt = pairs[idx]
            plant += plnt
            blooms = max(plant+grow,blooms)
            idx += 1

        return blooms
