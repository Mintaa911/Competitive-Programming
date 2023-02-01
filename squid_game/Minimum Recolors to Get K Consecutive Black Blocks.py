class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_op = 0
        start = end = 0
        ans = float('inf')
        while end < len(blocks):
            if blocks[end] == 'W':
                count_op += 1

            if (end - start + 1) == k:
                ans = min(ans,count_op)
                if blocks[start] == 'W':
                    count_op -= 1
                start += 1
            end += 1

        return ans
